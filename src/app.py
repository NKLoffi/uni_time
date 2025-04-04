import sys
from PyQt6.QtWidgets import QApplication
from ui import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    pass

if __name__ == "__main__":
    main()