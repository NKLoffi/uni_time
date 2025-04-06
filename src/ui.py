import sys
from PyQt6.QtWidgets import (QPushButton, QRadioButton, QLineEdit, QMainWindow, QWidget,
                             QLabel, QMessageBox)
from PyQt6.QtGui import QIcon
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

        # Settings Icon
        self.settingsButton = QPushButton(self)
        self.settingsButton.setIcon(QIcon("Assets/Settings_Icon.svg"))


        self.setStyleSheet(styles.WINDOW_STYLES)

        