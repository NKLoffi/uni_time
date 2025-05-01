from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from PyQt6 import uic

from database import Database
import styles
from .pages.welcome_page import create_welcome_page
from .pages.settings import create_settings_page
from .pages.create_account import create_account_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.db = Database()
        self.db.create_table()

        self.setWindowTitle("Uni Time")
        self.resize(800, 800)

        self.stack = QStackedWidget()
        self.initUI()

    def create_back_button(self, current, target):
        from PyQt6.QtWidgets import QPushButton, QHBoxLayout
        button = QPushButton()
        button.setIcon(QIcon("Assets/back_button.svg"))
        button.setObjectName("back")
        button.setGeometry(10, 10, 32, 32)
        button.clicked.connect(lambda: self.stack.setCurrentWidget(target))
        return button

    def create_settings_button(self):
        from PyQt6.QtWidgets import QPushButton
        button = QPushButton()
        button.setIcon(QIcon("Assets/Settings_Icon.svg"))
        button.setObjectName("settingsButton")
        button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settingsPage))

        return button

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.stack)

        self.welcomePage = create_welcome_page(self)
        self.createAcc = create_account_page(self)
        self.settingsPage = create_settings_page(self)

        self.stack.addWidget(self.welcomePage)
        self.stack.addWidget(self.createAcc)
        self.stack.addWidget(self.settingsPage)

        self.welcomePage.ui.pushButton_2.clicked.connect(lambda: self.stack.setCurrentWidget(self.createAcc))
        self.createAcc.ui.createAccButton.clicked.connect(self.create_account)
        self.createAcc.ui.backButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.welcomePage))
        self.welcomePage.ui.pushButton.clicked.connect(self.log_in)
        self.setStyleSheet(styles.WINDOW_STYLES)

    def create_account(self):
        full_name = self.createAcc.ui.nameField.text()
        email = self.createAcc.ui.emailField.text()
        password = self.createAcc.ui.passField.text()

        self.db.create_user(full_name, email, password)

        self.stack.setCurrentWidget(self.welcomePage)


    def log_in(self):
        email = self.welcomePage.ui.lineEdit.text()
        password = self.welcomePage.ui.lineEdit_2.text()

        user = self.db.user_log_in(email, password)

        if user:
            self.stack.setCurrentWidget(self.settingsPage)
        else:
            print("Invalid login credentials")