import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QDialog
from error import Ui_Dialog
from PyQt6.QtGui import *

class MainWindow:
    def __init__(self, errormsg):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)
        self.ui.textBrowser.setText(errormsg)
        self.main_win.setModal(True)
        self.css()

    def css(self):
        self.main_win.setWindowTitle("Data Manager Error Handler")

        self.main_win.setWindowIcon(QIcon("icons\loader.svg"))

    def show(self):
        self.main_win.show()

    def close(self):
        self.main_win.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())