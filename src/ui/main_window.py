from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QTableWidgetItem, QCheckBox, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QDate
from PyQt6 import uic

from database import Database
import styles
from .pages.welcome_page import create_welcome_page
from .pages.settings import create_settings_page
from .pages.create_account import create_account_page
from .pages.task import create_task_page

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
        from PyQt6.QtWidgets import QPushButton
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

        self.welcomePage.ui.passField.setEchoMode(QLineEdit.EchoMode.Password)
        self.createAcc = create_account_page(self)
        self.settingsPage = create_settings_page(self)
        self.createTaskPage = create_task_page(self)

        self.createTaskPage.ui.dueField.setDate(QDate.currentDate())


        self.stack.addWidget(self.welcomePage)
        self.stack.addWidget(self.createAcc)
        self.stack.addWidget(self.settingsPage)
        self.stack.addWidget(self.createTaskPage)

        self.welcomePage.ui.signupButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.createAcc))
        self.createAcc.ui.createAccButton.clicked.connect(self.create_account)
        self.createAcc.ui.backButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.welcomePage))
        self.welcomePage.ui.loginButton.clicked.connect(self.log_in)
        self.createTaskPage.ui.addButton.clicked.connect(self.create_task)
        self.createTaskPage.ui.deleteButton.clicked.connect(self.del_task)

        self.createTaskPage.ui.logOutButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.welcomePage)) # Have to make changes later



        self.setStyleSheet(styles.WINDOW_STYLES)

    def create_account(self):
        full_name = self.createAcc.ui.nameField.text()
        email = self.createAcc.ui.emailField.text()
        password = self.createAcc.ui.passField.text()
        cpassword = self.createAcc.ui.cPassField.text()

        if not (full_name and email and password and cpassword):
            QMessageBox.warning(self, "Inncomplete fields", "All fields are mandatory")
            return
        
        if  (password != cpassword):
            QMessageBox.warning(self, "Password Mismatch", "Passwords do not match.")
            return

        self.db.create_user(full_name, email, password)

        self.stack.setCurrentWidget(self.welcomePage)


    def log_in(self):
        email = self.welcomePage.ui.userField.text()
        password = self.welcomePage.ui.passField.text()

        if not (email and password):
            QMessageBox.warning(self, "Incomplete fields", "Please fill in all the fields")
            return

        user = self.db.user_log_in(email, password)

        if user:
            self.current_user_id = user[0]
            self.stack.setCurrentWidget(self.createTaskPage)
            self.load_tasks()
        else:
            print("Invalid login credentials")

    def create_task(self):
        course = self.createTaskPage.ui.courseField.text()
        assignment = self.createTaskPage.ui.AssignmentField.text()
        description = self.createTaskPage.ui.DescriptionField.text()
        due = self.createTaskPage.ui.dueField.text()

        self.db.insert_info(self.current_user_id, course, assignment, description, due)

        self.load_tasks()
        self.del_task()

    def load_tasks(self):
        tasks = self.db.get_tasks(self.current_user_id)
        self.createTaskPage.ui.taskTable.setRowCount(len(tasks))
        for row_id, task in enumerate(tasks):
            for col_id, value in enumerate(task[1:5]):
                item = QTableWidgetItem(str(value))
                if col_id == 0:
                    item.setData(Qt.ItemDataRole.UserRole, task[0])
                self.createTaskPage.ui.taskTable.setItem(row_id, col_id, item)

            checkbox = QCheckBox()
            self.createTaskPage.ui.taskTable.setCellWidget(row_id, 4, checkbox)

    def del_task(self):
        for row in reversed(range(self.createTaskPage.ui.taskTable.rowCount())):
            widget = self.createTaskPage.ui.taskTable.cellWidget(row, 4)
            if isinstance(widget, QCheckBox) and widget.isChecked():
                item = self.createTaskPage.ui.taskTable.item(row, 0)
                task_id = item.data(Qt.ItemDataRole.UserRole)
                self.db.dlt_task(task_id)
                self.createTaskPage.ui.taskTable.removeRow(row)
                print(f"Deleting task with ID: {task_id}")

    def log_out(self):
        pass