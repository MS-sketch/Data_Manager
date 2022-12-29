from folder_unit import Ui_Dialog
from PyQt6.QtWidgets import *
import sys
from PyQt6.QtGui import *
from passwordhelper import MainWindow_Password
from abouthelper import MainWindow_About


class MainWindow_Folder_Unit:
    def __init__(self, folder_name):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)

        self.icons(folder_name)

        self.ui.about.clicked.connect(self.open_about)

        self.ui.passwordgen.clicked.connect(self.open_pass)

        self.ui.passwordgen_2.clicked.connect(self.open_pass)

        # Defining Folder Layout
        self.folder_layout_Scroll = QVBoxLayout(self.ui.scrollAreaWidgetContents_3)

        self.entry_no = 0

        self.aboutwin = MainWindow_About()

        self.password_gen = MainWindow_Password()

        self.length_of_folder_name = None

    def open_pass(self):
        self.password_gen.show()

    def open_about(self):
        self.aboutwin.show()

    def view_data(self):
        pass

    def generate_btn(self):
        pass

    def refresh_btn(self):
        for i in reversed(range(self.folder_layout_Scroll.count())):
            self.folder_layout_Scroll.itemAt(i).widget().setParent(None)

        self.entry_no = 1
        self.generate_btn()

    def icons(self, folder_name):
        self.ui.main.setIcon(QIcon("icons/home.svg"))
        self.ui.vault_2.setIcon(QIcon("icons/database.svg"))
        self.ui.passwordgen.setIcon(QIcon("icons/key.svg"))
        self.ui.create_entry.setIcon(QIcon("icons/plus-circle.svg"))
        self.ui.about.setIcon(QIcon("icons/info.svg"))
        self.ui.create_entry_2.setIcon(QIcon("icons/plus-circle.svg"))
        self.ui.passwordgen_2.setIcon(QIcon("icons/key.svg"))
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.folder_name_var = ""
        self.length_of_folder_name = len(folder_name)

        if self.length_of_folder_name > 10:
            self.folder_name_var = folder_name[0:10] + ".."
        else:
            self.folder_name_var = folder_name
        self.folder_name1 = ""
        if self.length_of_folder_name > 30:
            self.folder_name1 = folder_name[0:30] + ""

        else:
            self.folder_name1 = folder_name

        self.main_win.setWindowTitle("Currently Open: " + str(self.folder_name1))
        self.ui.label.setText(str(self.folder_name_var))
        self.main_win.setWindowIcon(QIcon("icons/Win_icon.ico"))

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow_Folder_Unit()
    main_win.show()
    sys.exit(app.exec())
