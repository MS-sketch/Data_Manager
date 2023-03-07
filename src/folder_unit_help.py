from folder_unit import Ui_Dialog
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from passwordhelper import MainWindow_Password
from abouthelper import MainWindow_About
import entry_manager as en

class MainWindow_Folder_Unit:
    def __init__(self, folder_name, password, index):
        self.main_win = QDialog()
        self.user_interface = Ui_Dialog()
        self.user_interface.setupUi(self.main_win)

        self.icons(folder_name)

        self.user_interface.about.clicked.connect(self.open_about)

        self.user_interface.passwordgen.clicked.connect(self.open_pass)

        self.user_interface.passwordgen_2.clicked.connect(self.open_pass)

        # Defining Folder Layout
        self.folder_layout_Scroll = QVBoxLayout(self.user_interface.scrollAreaWidgetContents_3)

        self.entry_no = 0

        self.aboutwin = MainWindow_About()

        self.password_gen = MainWindow_Password()

        self.length_of_folder_name = None

        self.password = password

        self.indexx = index
        self.user_interface.main.setObjectName(str(folder_name))

        #self.user_interface.main.clicked.connect(self.execute)

    def execute(self):
        self.main_win.close()
        from vaulthelper import MainWindow
        self.main_vault = MainWindow(self.password)
        self.main_vault.delete_folder(self.user_interface.main.objectName(), self.indexx)
        #self.main_vault.show()

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
        self.user_interface.main.setIcon(QIcon("icons/trash.svg"))
        self.user_interface.main.setToolTip("Delete folder")
        self.user_interface.vault_2.hide()
        self.user_interface.passwordgen.setIcon(QIcon("icons/key.svg"))
        self.user_interface.create_entry.setIcon(QIcon("icons/plus-circle.svg"))
        self.user_interface.about.setIcon(QIcon("icons/info.svg"))
        self.user_interface.create_entry_2.setIcon(QIcon("icons/plus-circle.svg"))
        self.user_interface.passwordgen_2.setIcon(QIcon("icons/key.svg"))
        self.user_interface.stackedWidget.setCurrentWidget(self.user_interface.page)
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
        self.user_interface.label.setText(str(self.folder_name_var))
        self.main_win.setWindowIcon(QIcon("icons/Win_icon.ico"))

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow_Folder_Unit()
    main_win.show()
    sys.exit(app.exec())
