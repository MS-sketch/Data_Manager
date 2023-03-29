import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QDialog
from newauth import Ui_Dialog
import os
import hashlib
import passstrenght
from datetime import datetime
import entry_manager
import configparser
import config_manager


class MainWindow_auth:
    def __init__(self):
        self.win = None
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)

        entry_manager.index_entry()
        entry_manager.create_blank_table()
        config_manager.create_default_config()

        #Create Table Folder Struct.
        entry_manager.create_folder_index()

        #Bug Prob
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.master_password_single_user)

        #Calling The CSS
        self.iconfix()


        #Fixing The Time
        self.time()

        #If user forgot password
        self.ui.forgot_password.clicked.connect(self.reset)

        #If the user clicks create password
        self.ui.create_new_user_btn.clicked.connect(self.new_user)


        #Disabling the create btn
        self.ui.create_new_user_btn.setDisabled(True)

        #Calling the function to check if the btn is enabled.
        self.ui.create_single_user_password_line_1.textChanged.connect(self.enable_create)

        #Fixing Wrong Password
        self.login_ui()
        self.ui.master_password_single_user.textChanged.connect(self.login_ui)

        #Adding So when clicked login
        self.ui.unlock_btn.clicked.connect(self.login)

        #Reset Function
        self.ui.forgot_password.clicked.connect(self.forgot_pass)

        #Deining to connect to password info if pass info is clicked on the create menu in auth
        self.ui.pushButton_2.clicked.connect(self.show_password_info)


        master_pass_exist = entry_manager.master_existance()

        if master_pass_exist == False:
            self.new_user()


        else:
            self.ui.MainstackedWidget.setCurrentWidget(self.ui.login)
            self.login()


    def dev_mode(self):
        config_file = configparser.ConfigParser()
        config_file.read("config.ini")
        content = int(config_file.get('Dev', 'password_check'))

        if content == 1:
            return True

        else:
            return False

    def forgot_pass(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_7)
        self.reset()


    def login_ui(self):
        password_entered_by_usr = self.ui.master_password_single_user.text()
        if len(password_entered_by_usr) == 0:
            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
            self.ui.unlock_btn.setDisabled(True)
        else:
            self.ui.unlock_btn.setEnabled(True)


    def login(self):
        self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
        password_entered_by_usr = self.ui.master_password_single_user.text()
        if len(password_entered_by_usr) > 0:
            hashedpass = hashlib.sha256(password_entered_by_usr.encode("utf-8")).hexdigest()

            info2 = entry_manager.getmasterpassword(hashedpass)

            check = self.dev_mode()

            strength = passstrenght.passwordstrenght(password_entered_by_usr)

            if check == False:
                if strength == "weak":
                    text_limit = QMessageBox()
                    text_limit.setWindowIcon(QIcon("icons/info.svg"))
                    text_limit.setWindowTitle("Error")
                    text_limit.setText("An Error Occurred. \nError Code: 23")

                    text_limit.setStandardButtons(QMessageBox.StandardButton.Ok)
                    text_limit.setIcon(QMessageBox.Icon.Critical)
                    button = text_limit.exec()

                    if button == QMessageBox.StandardButton.Ok:
                        pass
                    sys.exit(23)

                else:
                    if info2:
                        self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
                        self.ui.forgot_password.setDisabled(True)
                        self.ui.unlock_btn.setDisabled(True)
                        self.ui.master_password_single_user.setDisabled(True)

                        self.open_vault(password_entered_by_usr)

                    else:
                        if len(password_entered_by_usr) > 0:
                            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.wrongpass_enter)

            if check == True:
                if info2:
                    self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
                    self.ui.forgot_password.setDisabled(True)
                    self.ui.unlock_btn.setDisabled(True)
                    self.ui.master_password_single_user.setDisabled(True)

                    self.open_vault(password_entered_by_usr)

                else:
                    if len(password_entered_by_usr) > 0:
                        self.ui.stackedWidgetmp.setCurrentWidget(self.ui.wrongpass_enter)

    def enable_create(self):
        password = self.ui.create_single_user_password_line_1.text()

        check = self.dev_mode()

        if check == True:
            self.ui.create_new_user_btn.setEnabled(True)

        else:
            if len(password) > 0:
                strength = passstrenght.passwordstrenght(password)

                if strength == "weak":
                    self.ui.substackedWidget.setCurrentWidget(self.ui.page_4)
                    self.ui.create_new_user_btn.setDisabled(True)

                elif strength == "moderate":
                    self.ui.substackedWidget.setCurrentWidget(self.ui.page_5)
                    self.ui.create_new_user_btn.setEnabled(True)

                elif strength == "strong":
                    self.ui.substackedWidget.setCurrentWidget(self.ui.page_6)
                    self.ui.create_new_user_btn.setEnabled(True)

            else:
                self.ui.create_new_user_btn.setDisabled(True)
                self.ui.substackedWidget.setCurrentWidget(self.ui.page_3)

    def new_user(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.newuser)

        self.ui.substackedWidget.setCurrentWidget(self.ui.page_3)

        newpass = self.ui.create_single_user_password_line_1.text()
        confirmpass = self.ui.create_single_user_password_confirm.text()

        newpass2 = len(newpass)

        if newpass2 > 0:
            if newpass == confirmpass:
                if newpass == "":
                    # No Blank Feilds Error
                    self.ui.substackedWidget.setCurrentWidget(self.ui.blank_feild)

                else:
                    # Pass Same Show Nothing
                    self.ui.substackedWidget.setCurrentWidget(self.ui.page_3)

                    hasheddata = hashlib.sha256(confirmpass.encode("utf-8")).hexdigest()

                    entry_manager.masterpasswordsave(hasheddata)

                    print(newpass)
                    self.open_vault(newpass)


            else:
                # Pass No Match
                self.ui.substackedWidget.setCurrentWidget(self.ui.pass_no_match)

        else:
            self.ui.substackedWidget.setCurrentWidget(self.ui.page_3)


    def open_vault(self, password):
        self.ui.unlock_btn.setText("Unlocking")
        from vaulthelper import MainWindow
        self.vault = MainWindow(password)
        self.vaultui = MainWindow(password)
        self.vaultui.show()
        self.main_win.close()

    def iconfix(self):
        self.main_win.setWindowIcon(QIcon("icons\Win_icon.ico"))
        self.main_win.setWindowTitle("Data Manager")


    def reset(self):
        
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_7)
        self.ui.create_new_user_btn_7.clicked.connect(self.warn_user_reset)
        self.ui.create_new_user_btn_8.clicked.connect(self.main_window)


    def main_window(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.login)
        self.login()

    def warn_user_reset(self):
        self.main_win.close()

        dlg = QMessageBox()
        dlg.setWindowIcon(QIcon("icons\info.svg"))
        dlg.setWindowTitle("Information")
        dlg.setText("The Vault Has Been Reset & Data Manager Is Now Exiting. \n Please Relaunch The App To Set It Up Again!")

        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            pass

        try:

            #Resetting doesn't work
            #Possible idea is to launch another process & terminate this process & delete the files.

            os.remove("usr_settings.db")
            os.remove("universal.key")
            os.remove("vault_data.db")

        except:
            return 1

        sys.exit()

    def time(self):
        now = datetime.now()
        integer_date = int(now.strftime("%H%M%S"))

        if integer_date < 120000:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_23)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_24)

    def show_password_info(self):
        from passwordstrengthhelper import MainWindow
        password = self.ui.create_single_user_password_line_1.text()
        lenofpass = len(password)

        if lenofpass > 0:
            self.win = MainWindow(password, 20000000000)  # defaut value
            self.win.show()

        else:
            error = QMessageBox()
            error.setWindowIcon(QIcon("icons\info.svg"))
            error.setWindowTitle("Information")
            error.setText("Not a valid number. \nError Code: 01")

            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setIcon(QMessageBox.Icon.Critical)
            button = error.exec()

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow_auth()
    main_win.show()
    sys.exit(app.exec())
