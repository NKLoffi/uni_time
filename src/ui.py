import sys
from PyQt6.QtWidgets import (QPushButton, QRadioButton, QLineEdit, QMainWindow, QWidget,
                             QLabel, QMessageBox, QVBoxLayout, QHBoxLayout, QGridLayout)
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


        self.introLabel = QLabel("Welcome to Uni Time") # have to define layout and add it
        self.introSubLabel = QLabel("Productivity is the key") # have to define layout and add it

        main_layout = QHBoxLayout()

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.introLabel) 
        layout.addWidget(self.introSubLabel)
        layout.addWidget(self.getStartedButton)
        self.introLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.introSubLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
        layout.setSpacing(4)

        main_layout.addLayout(layout)
        central_widget.setLayout(main_layout)        
        self.setStyleSheet(styles.WINDOW_STYLES)

        