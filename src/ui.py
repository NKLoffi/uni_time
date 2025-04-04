import sys
from PyQt6.QtWidgets import (QPushButton, QRadioButton, QLineEdit, QMainWindow, QWidget,
                             QLabel, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.db = Database()
        # self.db.create_table()

        self.setWindowTitle("Uni Time")
        self.resize(800, 800)

        self.initUI()
        

    def initUI(self):
        pass