from folder_unit import Ui_Dialog
from PyQt6.QtWidgets import *
import sys
from PyQt6.QtGui import *

class MainWindow_Folder_Unit:
    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)

        self.icons()

    def icons(self):
        self.ui.main.setIcon(QIcon("icons\home.svg"))
        self.ui.vault_2.setIcon(QIcon("icons\database.svg"))
        self.ui.passwordgen.setIcon(QIcon("icons\key.svg"))
        self.ui.create_entry.setIcon(QIcon("icons\plus-circle.svg"))
        self.ui.create_folder.setIcon(QIcon("icons/folder-plus.svg"))
        self.ui.about.setIcon(QIcon("icons\info.svg"))
        self.ui.create_folder_2.setIcon(QIcon("icons/folder-plus.svg"))
        self.ui.create_entry_2.setIcon(QIcon("icons\plus-circle.svg"))
        self.ui.passwordgen_2.setIcon(QIcon("icons\key.svg"))
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow_Folder_Unit()
    main_win.show()
    sys.exit(app.exec())