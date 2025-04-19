import sys
from PyQt6.QtWidgets import (QPushButton, QRadioButton, QLineEdit, QMainWindow, QWidget,
                             QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QStackedWidget)
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


    def create_back_button(self, current, target, stack):
        backButton = QPushButton()
        backButton.setIcon(QIcon("Assets/back_button.svg"))
        backButton.setObjectName("back")
        backButton.setGeometry(10, 10, 32, 32)
        backButton.clicked.connect(lambda: stack.setCurrentWidget(target))
        return backButton
    
    def create_settings_button(self):
        button = QPushButton()
        button.setIcon(QIcon("Assets/Settings_Icon.svg"))
        button.setObjectName("settingsButton")
        button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settingsPage))
        return button

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Stacked widget

        self.stack = QStackedWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stack)
        central_widget.setLayout(central_layout)

        self.getStartedButton = QPushButton("Get Started")
        self.getStartedButton.setObjectName("started")

        self.introLabel = QLabel("Welcome to Uni Time")
        self.introSubLabel = QLabel("Productivity is the key")

        # Get started page

        self.welcomePage = QWidget()
        welcome_layout = QVBoxLayout() # Main Layout

        top_bar_layout = QHBoxLayout() # Top Horizontal layout for settingsicon
        top_bar_layout.addStretch()
        top_bar_layout.addWidget(self.create_settings_button())
        welcome_layout.addLayout(top_bar_layout)

        welcomeH_layout = QHBoxLayout()
        welcomeH_layout.addStretch()

        welcome_layout.addStretch()
        welcome_layout.addWidget(self.introLabel)
        welcome_layout.addWidget(self.introSubLabel)
        welcomeH_layout.addWidget(self.getStartedButton)
        welcomeH_layout.addStretch()
        welcome_layout.addLayout(welcomeH_layout)

        # Get started page's intro

        self.introLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.introSubLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_layout.addStretch()
        welcome_layout.setSpacing(4) # spacing between the lines
        self.welcomePage.setLayout(welcome_layout)

        # Account creation Page

        self.createAccountPage = QWidget()
        second_layout = QVBoxLayout()

        # Create and add top bar with back button
        second_top_bar_layout = QHBoxLayout()
        self.backButton = self.create_back_button(self.createAccountPage, self.welcomePage, self.stack)
        second_top_bar_layout.addWidget(self.backButton)
        second_top_bar_layout.addStretch()
        second_top_bar_layout.addWidget(self.create_settings_button())
        second_layout.addLayout(second_top_bar_layout)
        # Add page label
        self.labels = {
            "fname": QLabel("Full Name: "),
            "Dob": QLabel("DOB: "),
            "email": QLabel("Email: "),
            "pass": QLabel("Password: "),
            "cpass": QLabel("Confirm Password: ")
        }

        self.text_boxes = {
            "fname": QLineEdit(self),
            "Dob": QLineEdit(self),
            "email": QLineEdit(self),
            "pass": QLineEdit(self),
            "cpass": QLineEdit(self),
        }

        placeholders = {
            "fname": "eg. John",
            "Dob": "eg. DD-MM-YYYY",
            "email": "jdoe@gmail.com",
            "pass": "Enter a password",
            "cpass": "Confirm your password"
        }

        for key, textbox in self.text_boxes.items():
            textbox.setPlaceholderText(placeholders[key])
            textbox.setMinimumWidth(200)
            textbox.setAlignment(Qt.AlignmentFlag.AlignLeft)

        second_label = QLabel("second page")
        second_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        second_layout.addWidget(second_label)
        self.createAccountPage.setLayout(second_layout)


        # Settings page

        self.settingsPage = QWidget()
        settings_layout = QVBoxLayout()

        settings_top_layout = QHBoxLayout()
        settings_back_button = self.create_back_button(self.settingsPage, self.welcomePage, self.stack)
        settings_top_layout.addWidget(settings_back_button)
        settings_top_layout.addStretch()

        settings_label = QLabel("Settings Page")
        settings_layout.addLayout(settings_top_layout)
        settings_layout.addWidget(settings_label)
        self.settingsPage.setLayout(settings_layout)


        self.stack.addWidget(self.welcomePage)
        self.stack.addWidget(self.createAccountPage)
        self.stack.addWidget(self.settingsPage)


        self.getStartedButton.clicked.connect(lambda: self.stack.setCurrentWidget(self.createAccountPage))

        self.setStyleSheet(styles.WINDOW_STYLES)