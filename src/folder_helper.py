from foldername_ui import Ui_Dialog
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Mainwindow_Folderdiag:

    def __init__(self):
        self.folder_name_diag_win = QDialog()
        self.folder_diag_ui = Ui_Dialog()
        self.folder_diag_ui.setupUi(self.folder_name_diag_win)

        self.folder_name_diag_win.setModal(True)

        self.folder_diag_ui.ok_btn.setDisabled(True)

        self.folder_diag_ui.lineEdit.textChanged.connect(self.disable_btn)

        self.css()

        self.folder_diag_ui.cancel_btn.clicked.connect(self.cancel)




    def disable_btn(self):
        if len(self.folder_diag_ui.lineEdit.text()) == 0:
            self.folder_diag_ui.ok_btn.setDisabled(True)

        else:
            self.folder_diag_ui.ok_btn.setEnabled(True)

    def css(self):
        self.folder_name_diag_win.setWindowTitle("Folder Name")
        self.folder_name_diag_win.setWindowIcon(QIcon("icons/folder-plus.svg"))


    def cancel(self):
        self.folder_name_diag_win.close()

    def show(self):
        self.folder_name_diag_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Mainwindow_Folderdiag()
    main_win.show()
    sys.exit(app.exec())