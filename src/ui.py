import sys
from PyQt6.QtWidgets import (QPushButton, QRadioButton, QLineEdit, QMainWindow, QWidget,
                             QLabel, QMessageBox, QVBoxLayout)
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

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)

        mainLayout = QVBoxLayout(mainWidget)
        
        centerLayout = QVBoxLayout()
        centerLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Settings Icon
        self.settingsButton = QPushButton(self)
        self.settingsButton.setIcon(QIcon("Assets/Settings_Icon.svg"))
        self.settingsButton.setObjectName("settingsButton")
        self.settingsButton.setGeometry(758, 10, 32, 32)

        self.introLabel = QLabel("Welcome to Uni Time") # have to define layout and add it
        self.introSubLabel = QLabel("Productivity is the key") # have to define layout and add it

        centerLayout.addWidget(self.introLabel)
        centerLayout.addWidget(self.introSubLabel)

        mainLayout.addStretch()
        mainLayout.addLayout(centerLayout)
        mainLayout.addStretch()

        
        self.setStyleSheet(styles.WINDOW_STYLES)

        