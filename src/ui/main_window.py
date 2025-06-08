from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QTableWidgetItem, QCheckBox, QLineEdit, QMessageBox, QComboBox, QFileDialog
from PyQt6.QtGui import QIcon, QRegularExpressionValidator
from PyQt6.QtCore import Qt, QDate, QRegularExpression, QDir
import csv
import bcrypt
from database import Database
import styles
from .pages.welcome_page import create_welcome_page
from .pages.settings import create_settings_page
from .pages.create_account import create_account_page
from .pages.task import create_task_page
from .pages.job import job_applications

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
        self.jobPortal = job_applications(self)

        self.createTaskPage.ui.dueField.setDate(QDate.currentDate())
        self.jobPortal.ui.aDateField.setDate(QDate.currentDate())


        self.stack.addWidget(self.welcomePage)
        self.stack.addWidget(self.createAcc)
        self.stack.addWidget(self.settingsPage)
        self.stack.addWidget(self.createTaskPage)
        self.stack.addWidget(self.jobPortal)

        self.welcomePage.ui.signupButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.createAcc))
        self.createAcc.ui.createAccButton.clicked.connect(self.create_account)
        self.createAcc.ui.backButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.welcomePage))
        self.welcomePage.ui.loginButton.clicked.connect(self.log_in)
        self.createTaskPage.ui.addButton.clicked.connect(self.create_task)
        self.jobPortal.ui.addButton.clicked.connect(self.create_jobs)
        self.createTaskPage.ui.deleteButton.clicked.connect(self.del_task)
        self.jobPortal.ui.pushButton.clicked.connect(self.dlt_jobs)
        self.createTaskPage.ui.jobBtn.clicked.connect(lambda: self.stack.setCurrentWidget(self.jobPortal))

        self.jobPortal.ui.backbtn.clicked.connect(lambda: self.stack.setCurrentWidget(self.createTaskPage))

        self.createTaskPage.ui.logOutButton.clicked.connect(self.log_out)

        self.jobPortal.ui.docbtn.clicked.connect(self.export_to_csv)

        


        self.setStyleSheet(styles.WINDOW_STYLES)

    def create_account(self):
        full_name = self.createAcc.ui.nameField.text()
        email = self.createAcc.ui.emailField.text()
        password = self.createAcc.ui.passField.text()
        cpassword = self.createAcc.ui.cPassField.text()

        salt = bcrypt.gensalt()

        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        if not (full_name and email and password and cpassword):
            QMessageBox.warning(self, "Incomplete fields", "All fields are mandatory")
            return
        
        if  (password != cpassword):
            QMessageBox.warning(self, "Password Mismatch", "Passwords do not match.")
            return
        
        email_regex = QRegularExpression(r"^[0-9a-zA-Z]+([._+-][0-9a-zA-Z]+)*@[0-9a-zA-Z]+([.-][0-9a-zA-Z]+)*\.[a-zA-Z]{2,}$")
        self.createAcc.ui.emailField.setValidator(QRegularExpressionValidator(email_regex))
        invalid_email = not email_regex.match(email).hasMatch()

        if invalid_email:
            QMessageBox.warning(self, "Invalid Email", "The email address you have entered is not valid")
            return
        self.db.create_user(full_name, email, hashed)

        self.stack.setCurrentWidget(self.welcomePage)

        self.clear_cacc_info()

    def clear_cacc_info(self):
        self.createAcc.ui.nameField.clear() 
        self.createAcc.ui.emailField.clear() 
        self.createAcc.ui.passField.clear() 
        self.createAcc.ui.cPassField.clear() 


    def log_in(self):
        email = self.welcomePage.ui.userField.text()
        password = self.welcomePage.ui.passField.text()

        email_regex = QRegularExpression(r"^[0-9a-zA-Z]+([._+-][0-9a-zA-Z]+)*@[0-9a-zA-Z]+([.-][0-9a-zA-Z]+)*\.[a-zA-Z]{2,}$")
        self.createAcc.ui.emailField.setValidator(QRegularExpressionValidator(email_regex))
        invalid_email = not email_regex.match(email).hasMatch()
        if invalid_email:
            QMessageBox.warning(self, "Invalid Email", "The email address you have entered is not valid")
            return
        
        
        if not (email and password):
            QMessageBox.warning(self, "Incomplete fields", "Please fill in all the fields")
            return

        user = self.db.user_log_in(email, password)


        if user:
            self.current_user_id = user[0]
            self.stack.setCurrentWidget(self.createTaskPage)
            self.load_tasks()
            self.load_jobs()
        else:
            QMessageBox.warning(self, "Invalid Credentials", "Your email or password is wrong")
            return
        

        
        self.clear_login_info()

    def clear_login_info(self):
        self.welcomePage.ui.userField.clear() 
        self.welcomePage.ui.passField.clear() 


    def create_task(self):
        course = self.createTaskPage.ui.courseField.text()
        assignment = self.createTaskPage.ui.AssignmentField.text()
        description = self.createTaskPage.ui.DescriptionField.text()
        due = self.createTaskPage.ui.dueField.text()

        if not(course and assignment and due):
            QMessageBox.warning(self, "Incomplete Fields", "To create a task you have to enter the course name, assignment name, and due date ")
            return
        
        self.db.insert_info(self.current_user_id, course, assignment, description, due)

        self.load_tasks()
        self.del_task()
        self.clear_task_fields()

    def clear_task_fields(self):
        self.createTaskPage.ui.courseField.clear()
        self.createTaskPage.ui.AssignmentField.clear()
        self.createTaskPage.ui.DescriptionField.clear()
        self.createTaskPage.ui.dueField.setDate(QDate.currentDate())

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
        self.current_user_id = None
        self.clear_job_field()
        self.clear_login_info()
        self.stack.setCurrentWidget(self.welcomePage)

    def create_jobs(self):
        job_id = self.jobPortal.ui.jobIdField.text()
        job_title = self.jobPortal.ui.JTitleField.text()
        comany_name = self.jobPortal.ui.CField.text()
        applied_date = self.jobPortal.ui.aDateField.text()
        notes = self.jobPortal.ui.notesField.text()

        if not job_title:
            QMessageBox.warning(self, "Incomplete Field", "Please entere the job title")
            return
        
        status = " "

        self.db.create_jobs(self.current_user_id, job_id, job_title, comany_name, applied_date, notes, status)

        self.load_jobs()

        self.clear_job_field()

    def clear_job_field(self):
        self.jobPortal.ui.jobIdField.clear()
        self.jobPortal.ui.JTitleField.clear()
        self.jobPortal.ui.CField.clear()
        self.jobPortal.ui.aDateField.setDate(QDate.currentDate())
        self.jobPortal.ui.notesField.clear()
    
    def load_jobs(self):
        jobs = self.db.get_jobs(self.current_user_id)
        self.jobPortal.ui.jobTable.setRowCount(len(jobs))

        for row_id, job in enumerate(jobs):
            for col_id, value in enumerate(job):
                if col_id == 5:
                    continue
                item = QTableWidgetItem(str(value))
                if col_id == 0:
                    item.setData(Qt.ItemDataRole.UserRole, job[0])
                self.jobPortal.ui.jobTable.setItem(row_id, col_id, item)

            comboBox = QComboBox()
            comboBox.addItems(['Applied', 'Interviewed', 'Received Offer' ,'Rejected'])
            comboBox.setCurrentText(job[5])
            id = job[0]
            self.connect_status_change(comboBox, id)
            self.jobPortal.ui.jobTable.setCellWidget(row_id, 5, comboBox)

            checkbox = QCheckBox()
            self.jobPortal.ui.jobTable.setCellWidget(row_id, 6, checkbox)

    def connect_status_change(self, comboBox, job_id):
        comboBox.currentTextChanged.connect(lambda status: self.update_job_status(job_id, status))

    def update_job_status(self, job_id, status):
            self.db.update_job_status(job_id, status)

    
    def dlt_jobs(self):
        for row in reversed(range(self.jobPortal.ui.jobTable.rowCount())):
            widget = self.jobPortal.ui.jobTable.cellWidget(row, 6)
            if isinstance(widget, QCheckBox) and widget.isChecked():
                item = self.jobPortal.ui.jobTable.item(row, 0)
                job_id = item.data(Qt.ItemDataRole.UserRole)
                self.db.dlt_job(job_id)
                self.jobPortal.ui.jobTable.removeRow(row)

    def export_to_csv(self):
        path = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/export.csv", "CSV Files(*.csv *.txt)")
        if path[0]:
            with open(path[0], mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                headers = []
                for column in range(self.jobPortal.ui.jobTable.columnCount() - 1):  
                    item = self.jobPortal.ui.jobTable.horizontalHeaderItem(column)
                    headers.append(item.text() if item else f"Column {column}")
                writer.writerow(headers)

                for row in range(self.jobPortal.ui.jobTable.rowCount()):
                    row_data = []
                    for column in range(self.jobPortal.ui.jobTable.columnCount() - 1):
                        widget = self.jobPortal.ui.jobTable.cellWidget(row, column)
                        if isinstance(widget, QComboBox):
                            row_data.append(widget.currentText())
                        else:
                            item = self.jobPortal.ui.jobTable.item(row, column)
                            row_data.append(item.text() if item else "")
                    writer.writerow(row_data)