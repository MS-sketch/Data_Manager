import sys
import dataencryptor
import entry_manager
from vaultui import Ui_MainWindow
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from abouthelper import MainWindow_About
from passwordhelper import MainWindow_Password
import entry_manager as en
from folder_unit_help import MainWindow_Folder_Unit
from folder_helper import Mainwindow_Folderdiag
from authcheck import MainWindow_auth
import configparser


class MainWindow:
    def __init__(self, password):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.iconfix()

        # Encryption Key Create.
        dataencryptor.keychk()

        self.ui.scrollArea_3.setWidgetResizable(True)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(1)

        self.lay = QVBoxLayout(self.ui.scrollAreaWidgetContents_3)

        self.ui.create_entry.clicked.connect(self.new_entry)

        self.ui.discard.clicked.connect(self.discard)

        self.ui.passwordgen.clicked.connect(self.open_password_gen)

        self.ui.about.clicked.connect(self.open_about)

        self.ui.reset.clicked.connect(self.btn_reset)

        self.ui.create_folder.clicked.connect(self.open_newfolder)

        self.window_for_newfolder = Mainwindow_Folderdiag()

        self.window_for_newfolder.folder_diag_ui.ok_btn.clicked.connect(self.create_new_folder)

        self.floder_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents_2)

        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.main_2.clicked.connect(self.lock_vault)

        # Creating Buttons
        self.entry_number = 1
        self.make_btn()

        # Stopping Recursion
        self.btn_id = 0

        # Setting Button Edit Function
        self.ui.save_btn_3.clicked.connect(lambda: self.edit_mode())

        self.ui.create_folder_2.clicked.connect(self.open_newfolder)

        self.ui.create_entry_2.clicked.connect(self.new_entry)

        self.ui.passwordgen_2.clicked.connect(self.open_password_gen)

        self.ui.reset_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))

        self.ui.save_btn.clicked.connect(self.save_chk)

        self.current_id = 0

        self.ui.discard_2.clicked.connect(self.delete_entry_from_default)

        self.current_title = ""

        # Defining the variables & init of the other ui elements
        self.window_for_auth = MainWindow_auth()
        self.window_for_pass = MainWindow_Password()
        self.window_for_about = MainWindow_About()

        self.spawn_folder_items()

    def refresh_folder_area(self):
        for i in reversed(range(self.floder_layout.count())):
            self.floder_layout.itemAt(i).widget().setParent(None)
        self.spawn_folder_items()

    def spawn_folder_object(self, name):
        if len(name) > 17:
            newBtn = QPushButton(str(name[0:17]) + "...")

        else:
            newBtn = QPushButton(str(name))

        newBtn.setObjectName(str(name))
        newBtn.clicked.connect(lambda: self.open_folder_contents(newBtn.objectName()))
        self.floder_layout.addWidget(newBtn)
        self.add_new_items_in_combo_box(name)

    def spawn_folder_items(self):
        folder_name = en.fetch_from_folder_index()
        for x in range(len(folder_name)):
            self.spawn_folder_object(folder_name[x][0])

    def add_new_items_in_combo_box(self, name):
        folder_items = []
        x = 0
        while True:
            y = self.ui.comboBox.itemText(x)
            if y == '':
                break
            folder_items.append(y)
            x += 1
        if name not in folder_items:
            # Adding the folder name to the combobox choice.
            self.ui.comboBox_2.addItem(str(name))
            self.ui.comboBox.addItem(str(name))

    def save_folder_data(self, folder_name):
        pass

    def save_chk(self):
        where_to_save = str(self.ui.comboBox.currentText())

        if where_to_save == "No Folder":
            self.create_new_entry_in_default()

        if where_to_save == "Create A New Folder":
            input_barrier = self.data_check()

            if input_barrier:
                self.open_newfolder()

    def entry_saved(self, entry_name, type_save):
        text_limit = QMessageBox()
        text_limit.setWindowIcon(QIcon("icons/info.svg"))
        text_limit.setWindowTitle("Entry " + str(type_save) + "!")

        if len(entry_name) > 17:
            text_limit.setText(
                "Your entry named '" + str(entry_name[0:16]) + "...' has been successfully " + str(type_save) + ".")

        elif len(entry_name) < 17:
            text_limit.setText(
                "Your entry named '" + str(entry_name) + "' has been successfully " + str(type_save) + ".")

        text_limit.setStandardButtons(QMessageBox.StandardButton.Ok)
        text_limit.setIcon(QMessageBox.Icon.Information)
        button = text_limit.exec()

        if button == QMessageBox.StandardButton.Ok:
            pass

        text_limit.close()

        self.refresh_scroll_area()

    def data_check(self):
        warning_no_filled = ""
        if len(self.ui.lineEdit_2.text()) == 0:
            warning_no_filled = warning_no_filled + "Title"

        if len(self.ui.web_address.text()) == 0:
            if len(warning_no_filled) == 0:
                warning_no_filled = warning_no_filled + "Web Site"
            else:
                warning_no_filled = warning_no_filled + ", Web Site"

        if len(self.ui.user_name.text()) == 0:
            if len(warning_no_filled) == 0:
                warning_no_filled = warning_no_filled + "User Name"
            else:
                warning_no_filled = warning_no_filled + ", User Name"

        if len(self.ui.lineEdit_3.text()) == 0:
            if len(warning_no_filled) == 0:
                warning_no_filled = warning_no_filled + "Password"

            else:
                warning_no_filled = warning_no_filled + ", Password"

        if len(warning_no_filled) > 0:
            text_limit = QMessageBox()
            text_limit.setWindowIcon(QIcon("icons/info.svg"))
            text_limit.setWindowTitle("Required Fields Missing")
            text_limit.setText("Please fill out the necessary fields to save the entry. \n"
                               "You have not filled the following fields: " + warning_no_filled)

            text_limit.setStandardButtons(QMessageBox.StandardButton.Ok)
            text_limit.setIcon(QMessageBox.Icon.Warning)
            button = text_limit.exec()

            if button == QMessageBox.StandardButton.Ok:
                pass

            text_limit.close()

        else:
            return True

    def delete_entry_from_default(self):
        text_limit = QMessageBox()
        text_limit.setWindowIcon(QIcon("icons/info.svg"))
        text_limit.setWindowTitle("Delete Entry")
        text_limit.setText("Are you sure you want to delete this entry? \n"
                           "DELETED ENTRIES CAN'T BE RECOVERED.")

        text_limit.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        text_limit.setIcon(QMessageBox.Icon.Warning)
        button = text_limit.exec()

        if button == QMessageBox.StandardButton.Yes:
            en.delete_from_index(self.current_id)
            en.delete_entry_from_default(self.current_id)
            self.refresh_scroll_area()
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        text_limit.close()

    def temp(self):
        self.ui.save_btn_2.clicked.connect(lambda: self.save_exec())

    def save_exec(self):
        self.update_entry(self.btn_id)
        self.read_mode()

    def edit_mode(self):
        self.enable_edit()

        self.set_all_disabled()

    def enable_edit(self):
        self.btn_id = int(self.ui.save_btn_3.objectName())
        self.temp()

        entry_point = en.fetch_from_default(int(self.ui.save_btn_3.objectName()))
        title = entry_point[1]
        website = entry_point[2]
        is_default = entry_point[3]
        usr_name = entry_point[4]
        password = entry_point[5]
        notes = entry_point[6]

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

        self.ui.stackedWidget_3.setCurrentWidget(self.ui.edit_save)

        self.ui.lineEdit_2.setText(str(title))
        self.ui.web_address.setText(str(website))
        self.ui.user_name.setText(str(usr_name))
        self.ui.lineEdit_3.setText(str(password))
        self.ui.notes.setText(str(notes))

        if int(is_default) == 0:
            self.ui.primary_websitedomain.setChecked(True)

        else:
            self.ui.primary_websitedomain.setChecked(False)

    def set_entry_onsc(self, id):
        id2 = self.ui.save_btn_3.setObjectName(str(id))
        self.current_id = id
        self.btn_id = id2
        self.temp()

        self.enable_edit()

        self.read_mode()

    def read_mode(self):
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_11)
        self.ui.lineEdit_2.setReadOnly(True)
        self.ui.web_address.setReadOnly(True)
        self.ui.user_name.setReadOnly(True)
        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.notes.setReadOnly(True)
        self.ui.primary_websitedomain.hide()

    def spawn(self, name, id):

        if len(name) > 17:
            newBtn = QPushButton(str(name[0:17]) + "...")

        else:
            newBtn = QPushButton(str(name))

        newBtn.setObjectName(str(id))
        newBtn.clicked.connect(lambda: self.set_entry_onsc(newBtn.objectName()))
        self.lay.addWidget(newBtn)

    def make_btn(self):
        index = en.fetch_all_from_index_entry()

        if len(index) == 0:
            self.ui.label_8.setText("Your Vault Is Empty")

        elif len(index) > 0:
            yz_var = index[len(index) - 1]
            self.entry_number = int(yz_var[0])

            self.ui.label_8.setText("Open An Entry Or Create A New One.")

            for x in range(len(index)):
                y = index[x]
                entry = en.fetch_from_default(y[0])
                self.spawn(entry[1], y[0])

    def enable_save(self):
        self.btn_id = -1

    def update_entry(self, id):
        # Will add an if statement to check if the entry is in default.

        if self.btn_id != 0:
            title = self.ui.lineEdit_2.text()
            website = self.ui.web_address.text()
            usr_name = self.ui.user_name.text()
            password = self.ui.lineEdit_3.text()
            notes = self.ui.notes.toPlainText()

            if self.ui.primary_websitedomain.isChecked():
                ischeck = 0

            else:
                ischeck = 1

            entry_manager.update_create_entry(id, title, website, ischeck, usr_name, password, notes)

            self.btn_id = 0

            self.refresh_scroll_area()

    def refresh_scroll_area(self):
        for i in reversed(range(self.lay.count())):
            self.lay.itemAt(i).widget().setParent(None)

        self.entry_number = 1
        self.make_btn()

    def create_new_entry_in_default(self):

        input_barrier = self.data_check()

        if input_barrier:
            if self.ui.primary_websitedomain.isChecked():
                ischeck = 0

            else:
                ischeck = 1

            id_no = int(self.entry_number) + 1
            print(id_no)

            title = self.ui.lineEdit_2.text()
            website = self.ui.web_address.text()
            usr_name = self.ui.user_name.text()
            password = self.ui.lineEdit_3.text()
            notes = self.ui.notes.toPlainText()

            en.insert_in_default(id_no, title, website, ischeck, usr_name, password, notes)

            self.ui.stackedWidget.setCurrentWidget(self.ui.page)

            self.entry_number = id_no

            en.insert_into_index(id_no)

            self.entry_saved(title, "saved")

    def iconfix(self):
        self.ui.main.setIcon(QIcon("icons/home.svg"))
        self.ui.vault_2.setIcon(QIcon("icons/database.svg"))
        self.ui.passwordgen.setIcon(QIcon("icons/key.svg"))
        self.ui.create_entry.setIcon(QIcon("icons/plus-circle.svg"))
        self.ui.create_folder.setIcon(QIcon("icons/folder-plus.svg"))
        self.ui.settings.setIcon(QIcon("icons/settings.svg"))
        self.ui.about.setIcon(QIcon("icons/info.svg"))
        self.ui.main_2.setIcon(QIcon("icons/lock.svg"))
        self.ui.save_btn.setIcon(QIcon("icons/save.svg"))
        self.ui.discard.setIcon(QIcon("icons/file-minus.svg"))
        self.ui.reset.setIcon(QIcon("icons/repeat.svg"))
        self.ui.pushButton.setIcon(QIcon("icons/eye.svg"))
        self.ui.pushButton_2.setIcon(QIcon("icons/eye-off.svg"))
        self.ui.pushButton_2.setText("")
        self.ui.pushButton.setText("")
        self.ui.save_btn.setStatusTip("Save Your Work.")
        self.ui.discard.setStatusTip("Discard Your Done Work.")
        self.ui.reset.setStatusTip("Reset All The Fields.")
        self.main_win.setWindowIcon(QIcon("icons/Win_icon.ico"))
        self.main_win.setWindowTitle("Data Manager")
        self.ui.save_btn_2.setIcon(QIcon("icons/save.svg"))
        self.ui.discard_2.setIcon(QIcon("icons/delete.svg"))
        self.ui.reset_2.setIcon(QIcon("icons/file-minus.svg"))
        self.ui.create_entry_2.setIcon(QIcon("icons/plus-circle.svg"))
        self.ui.create_folder_2.setIcon(QIcon("icons/folder-plus.svg"))
        self.ui.passwordgen_2.setIcon(QIcon("icons/key.svg"))
        self.ui.save_btn_3.setIcon(QIcon("icons/pen-tool.svg"))

    def new_entry(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.new_save)
        self.set_all_disabled()
        self.reset_all()

    def set_all_disabled(self):
        self.ui.lineEdit_2.setReadOnly(False)
        self.ui.web_address.setReadOnly(False)
        self.ui.user_name.setReadOnly(False)
        self.ui.lineEdit_3.setReadOnly(False)
        self.ui.notes.setReadOnly(False)
        self.ui.primary_websitedomain.show()
        self.ui.stackedWidget_4.setCurrentWidget(self.ui.page_10)

    def reset_all(self):
        self.ui.lineEdit_2.setText("")
        self.ui.web_address.setText("")
        self.ui.user_name.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.notes.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.primary_websitedomain.setChecked(True)

    def btn_reset(self):
        title_len = len(self.ui.lineEdit_2.text())

        website_len = len(self.ui.web_address.text())

        user_len = len(self.ui.user_name.text())

        password_len = len(self.ui.lineEdit_3.text())

        notes_len = len(self.ui.notes.toPlainText())

        if title_len > 0 or website_len > 0 or user_len > 0 or password_len > 0 or notes_len > 0:
            text_limit = QMessageBox()
            text_limit.setWindowIcon(QIcon("icons/info.svg"))
            text_limit.setWindowTitle("Confirmation")
            text_limit.setText("Do want to start over again?")

            text_limit.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            text_limit.setIcon(QMessageBox.Icon.Warning)
            button = text_limit.exec()

            if button == QMessageBox.StandardButton.Yes:
                self.reset_all()
            text_limit.close()

    def discard(self):
        title_len = len(self.ui.lineEdit_2.text())

        website_len = len(self.ui.web_address.text())

        user_len = len(self.ui.user_name.text())

        password_len = len(self.ui.lineEdit_3.text())

        notes_len = len(self.ui.notes.toPlainText())

        if title_len > 0 or website_len > 0 or user_len > 0 or password_len > 0 or notes_len > 0:
            text_limit = QMessageBox()
            text_limit.setWindowIcon(QIcon("icons/info.svg"))
            text_limit.setWindowTitle("Confirmation")
            text_limit.setText("Do you want to save your entry?")

            text_limit.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            text_limit.setIcon(QMessageBox.Icon.Warning)
            button = text_limit.exec()

            if button == QMessageBox.StandardButton.No:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page)
                self.reset_all()

            text_limit.close()

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def open_password_gen(self):
        self.window_for_pass.show()

    def open_about(self):
        self.window_for_about.show()

    def open_newfolder(self):
        self.ui_for_newfolder = Mainwindow_Folderdiag()
        self.window_for_newfolder.show()

    def create_new_folder(self):
        folder_name_fromstr = self.window_for_newfolder.folder_diag_ui.lineEdit.text()

        folder_name_len = len(folder_name_fromstr)

        # Opening the config file.
        config_file = configparser.ConfigParser()
        config_file.read("config.ini")
        content = config_file.get('Limits', 'folder_name_limit')

        if folder_name_len > int(content):
            text_limit = QMessageBox()
            text_limit.setWindowIcon(QIcon("icons/info.svg"))
            text_limit.setWindowTitle("Length Character Error")
            text_limit.setText(
                "The length of the folder name should be less than " + content + " Characters including spaces. \n"
                                                                                 "Note: You may modify this setting by changing the settings.")

            text_limit.setStandardButtons(QMessageBox.StandardButton.Ok)
            text_limit.setIcon(QMessageBox.Icon.Warning)
            button = text_limit.exec()

            if button == QMessageBox.StandardButton.Ok:
                pass
            self.window_for_newfolder.folder_diag_ui.lineEdit.setText("")
            text_limit.close()

        else:
            invalid_names = ["No Folder", "Create A New Folder", "Same", "main"]

            for x in range(len(invalid_names)):
                if folder_name_fromstr == invalid_names[x]:
                    name_exception = QMessageBox()
                    name_exception.setWindowIcon(QIcon("icons/info.svg"))
                    name_exception.setWindowTitle("Reserved Name Error")
                    name_exception.setText("You have typed a name which is reserved for the application. \n"
                                           "RESERVED NAMES can't be used as folder or entry names.")

                    name_exception.setStandardButtons(QMessageBox.StandardButton.Ok)
                    name_exception.setIcon(QMessageBox.Icon.Critical)
                    button = name_exception.exec()

                    if button == QMessageBox.StandardButton.Ok:
                        pass
                    self.window_for_newfolder.folder_diag_ui.lineEdit.setText("")
                    name_exception.close()

                    folder_name_fromstr = ""

                if folder_name_fromstr == "":
                    break

                if folder_name_fromstr != "":
                    print(folder_name_fromstr)
                    try:
                        en.insert_special_folder_index(str(folder_name_fromstr))
                        self.window_for_newfolder.folder_diag_ui.lineEdit.setText("")
                        self.window_for_newfolder.folder_name_diag_win.close()
                        self.refresh_folder_area()
                        break
                    except:
                        name_exception = QMessageBox()
                        name_exception.setWindowIcon(QIcon("icons/info.svg"))
                        name_exception.setWindowTitle("Repeated Name")
                        name_exception.setText("A folder of same name already exists!")

                        name_exception.setStandardButtons(QMessageBox.StandardButton.Ok)
                        name_exception.setIcon(QMessageBox.Icon.Critical)
                        button = name_exception.exec()

                        if button == QMessageBox.StandardButton.Ok:
                            pass
                        self.window_for_newfolder.folder_diag_ui.lineEdit.setText("")
                        name_exception.close()

                        folder_name_fromstr = ""

            else:
                pass

    def open_folder_contents(self, btn_name):
        self.window_folder_pop = MainWindow_Folder_Unit(btn_name)
        self.window_folder_pop.show()

    def lock_vault(self):
        # Encrypt Function.
        self.main_win.close()
        try:
            self.window_for_pass.close()
            self.window_for_about.close()

        except:
            try:
                self.window_for_about.close()
            except:
                pass

        self.window_for_auth.show()

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
