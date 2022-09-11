import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QDialog
import existance
from error import Ui_Dialog
import os
import pickle
import random
import hashlib
import shutil
import encryptionmodule

class MainWindow:
    def __init__(self, errormsg):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)
        self.ui.textBrowser.setText(errormsg)
        self.main_win.setModal(True)


    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())