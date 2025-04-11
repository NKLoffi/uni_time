import sys
from PyQt6.QtWidgets import (QPushButton, QRadioButton, QLineEdit, QMainWindow, QWidget,
                             QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from database import Database
import styles

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.db.create_table()

        self.setWindowTitle("Uni Time")
        self.resize(800, 800)

        self.initUI()
        

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Settings Icon
        self.settingsButton = QPushButton(self)
        self.settingsButton.setIcon(QIcon("Assets/Settings_Icon.svg"))
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setGeometry(758, 10, 32, 32)

        self.getStartedButton = QPushButton("Get Started")
        self.getStartedButton.setObjectName("started")

        self.introLabel = QLabel("Welcome to Uni Time")
        self.introSubLabel = QLabel("Productivity is the key")


        self.stack = QStackedWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stack)
        central_widget.setLayout(central_layout)


        self.welcomePage = QWidget()
        welcome_layout = QVBoxLayout()
        welcome_layout.addStretch()
        welcome_layout.addWidget(self.introLabel)
        welcome_layout.addWidget(self.introSubLabel)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.getStartedButton)
        button_layout.addStretch()
        welcome_layout.addLayout(button_layout)

        self.introLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.introSubLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_layout.addStretch()
        welcome_layout.setSpacing(4)
        self.welcomePage.setLayout(welcome_layout)


        self.secondPage = QWidget()
        second_layout = QVBoxLayout()
        second_label = QLabel("second page")
        second_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        second_layout.addWidget(second_label)
        self.secondPage.setLayout(second_layout)

        self.backButton = QPushButton(self)
        self.backButton.setIcon(QIcon("Assets/back_button.svg"))
        self.backButton.setObjectName("back")
        self.backButton.setGeometry(10, 10, 32, 32)
        self.backButton.clicked.connect(lambda:self.stack.setCurrentWidget(self.welcomePage))

        self.stack.addWidget(self.welcomePage)
        self.stack.addWidget(self.secondPage)


        self.getStartedButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.secondPage))

        self.setStyleSheet(styles.WINDOW_STYLES)