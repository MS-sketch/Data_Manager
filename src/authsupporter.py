"""
This module is the first one to start in the program.
It takes in the user credentials for creation of vault/login & sees if the credentials are correct.
They are stored in a database by hashing, So it is very hard to crack.

"*Before 2 Years God & I know what this code was doing now only God knows what does the code does.*
~ Mainakh Sarkar In 2024 ;)"
"""


#Importing all the stuff
import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QDialog
import existance
import sqlmanagerhelper
from authentication import Ui_Dialog
import os
import hashlib
import passstrenght
from PyQt6 import QtWidgets
from datetime import datetime

database_existence = existance.exists("usr_settings.db")
password_vault = existance.exists("password.txt.aes")


class MainWindow:
    def __init__(self):
        self.win = None
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)

        self.iconfix()

        # temporary multi_user disable
        # self.ui.multi_user.setDisabled(True)

        # Tells User How Strong Is Password.
        self.ui.create_single_user_password_line_1.textChanged.connect(self.setpassstrenght)

        self.ui.pushButton_2.clicked.connect(self.passinfo)

        self.ui.admin_username.textChanged.connect(self.admin_multiple)
        self.ui.unlock_btn.setDisabled(True)

        self.ui.create_new_user_btn.clicked.connect(self.newusr)

        # SPELLING CHECK
        self.ui.label_17.setText("Please Select Your Preferred Choice")
        self.ui.label_18.setText("The Multiple Users Feature Is Work In Progress.  Build Version: 1.9")

        self.ui.admin_password.setDisabled(True)
        self.ui.admin_confirm_password.setDisabled(True)

        self.ui.admin_create_account.setDisabled(True)
        self.ui.create_new_user_btn.setDisabled(True)

        self.ui.admin_password_info.clicked.connect(self.passinfo2)

        self.ui.add_usr_password_info.clicked.connect(self.passinfo3)

        self.ui.admin_username.setText("administrator")
        self.ui.label_44.setText("Please Create An Administrator Account.")

        # Time Fix
        self.time()

        # print(type(os.stat("usr_settings.db").st_size))

        if database_existence == "TRUE":
            if os.stat("usr_settings.db").st_size == 0:
                self.preffered_mode()

            elif os.stat("usr_settings.db").st_size > 0:
                type1 = sqlmanagerhelper.table_check()
                print(type1)

                if type1 == "single_user":
                    info5 = str(sqlmanagerhelper.dynamic_table_fetch("type", "method", "usr_settings.db"))
                    if info5:
                        if str(info5) == "[('False',)]" or str(info5) == "[]":
                            self.more()

                        else:
                            self.ui.MainstackedWidget.setCurrentWidget(self.ui.login)
                            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
                            self.ui.master_password_single_user.textChanged.connect(self.loginusr)
                            self.ui.unlock_btn.clicked.connect(self.login2)
                            self.ui.forgot_password.clicked.connect(self.reset)

                            self.ui.create_new_user_btn_7.clicked.connect(self.warn)

                    else:
                        sqlmanagerhelper.type("False")
                        self.more()

                elif type1 == "multiple_user":
                    self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_26)

                if type1 == "nothing":
                    print("WHY ARE YOU HERE?")

        if database_existence == "FALSE":
            print("OK")
            self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_7)
            self.ui.okaybutton_2.clicked.connect(self.preffered_mode)



    def passinfo3(self):
        from passwordstrengthhelper import MainWindow
        password = self.ui.add_usr_password.text()
        lenofpass = len(password)

        if lenofpass > 0:
            self.win = MainWindow(password, 20000000000)
            self.win.show()


    def reset_vault(self):
        pass

    def reset(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_25)
        self.ui.create_new_user_btn_8.setText("Back")
        self.ui.create_new_user_btn_8.clicked.connect(self.loginusr)

    def newusr2(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_8)

        self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_17)

        newpass = self.ui.admin_password.text()
        confirmpass = self.ui.admin_confirm_password.text()

        newpass2 = len(newpass)

        if newpass2 > 0:
            if newpass == confirmpass:
                if newpass == "":
                    # No Blank Feilds Error
                    self.ui.substackedWidget_3.setCurrentWidget(self.ui.blank_feild_3)

                else:
                    # Pass Same Show Nothing

                    #for testing purposes the below is disabled.
                    #self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_17)

                    #hasheddata = hashlib.sha256(confirmpass.encode("utf-8")).hexdigest()

                    #print(hasheddata)

                    #self.more()

                    self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_21)

                    self.ui.not_add_more_users.clicked.connect(self.more)

                    self.ui.add_more_users.clicked.connect(self.add_more_users)

            else:
                # Pass No Match
                self.ui.substackedWidget_3.setCurrentWidget(self.ui.pass_no_match_3)

        else:
            self.ui.substackedWidget_3.setCurrentWidget(self.ui.blank_feild_3)

    def add_more_users_chk(self):
        length_of_usr_name = len(self.ui.add_usr_new_name.text())

        if length_of_usr_name > 0:
            self.ui.add_usr_password.setEnabled(True)
            self.ui.add_usr_confirm_pass.setEnabled(True)

            length_of_password = len(self.ui.add_usr_password.text())
            length_of_check_pass = len(self.ui.add_usr_confirm_pass.text())

            if length_of_password > 0:
                strength = passstrenght.passwordstrenght(self.ui.add_usr_password.text())

                if strength == "weak":
                    pass

                elif strength == "moderate" or strength == "strong":
                    self.ui.create_more_usr_btn.setEnabled(True)

            else:
                self.ui.create_more_usr_btn.setDisabled(True)

        elif length_of_usr_name <= 0:
            self.ui.create_more_usr_btn.setDisabled(True)
            self.ui.add_usr_password.setText("")
            self.ui.add_usr_password.setDisabled(True)
            self.ui.add_usr_confirm_pass.setText("")
            self.ui.add_usr_confirm_pass.setDisabled(True)



    def add_more_users(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_22)
        self.ui.create_more_usr_btn.setDisabled(True)

        self.ui.add_usr_password.setDisabled(True)
        self.ui.add_usr_confirm_pass.setDisabled(True)

        self.ui.add_usr_new_name.textChanged.connect(self.add_more_users_chk)

        self.ui.add_usr_password.textChanged.connect(self.add_more_users_chk)

    def time(self):
        now = datetime.now()
        integer_date = int(now.strftime("%H%M%S"))

        if integer_date < 120000:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_23)

        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_24)

    def multiusr(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_8)
        self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_17)

        self.ui.back_to_usr_sel_from_admin.clicked.connect(self.back1)

        self.ui.admin_create_account.clicked.connect(self.newusr2)

    def preffered_mode(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_7)
        single_usr = str(self.ui.single_user.isChecked())
        multi_usr = str(self.ui.multi_user.isChecked())

        if single_usr == "True":

            self.newusr()

        if multi_usr == "True":
            self.multiusr()

    def login2(self):
        password_entered_by_usr = self.ui.master_password_single_user.text()
        hashedpass = hashlib.sha256(password_entered_by_usr.encode("utf-8")).hexdigest()

        info2 = sqlmanagerhelper.getmasterpassword(hashedpass)

        if info2:
            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
            self.ui.forgot_password.setDisabled(True)
            self.ui.unlock_btn.setDisabled(True)
            self.ui.master_password_single_user.setDisabled(True)
            print("Ok")

        else:
            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.wrongpass_enter)

    def loginusr(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.login)

        password_entered_by_usr = self.ui.master_password_single_user.text()

        if len(password_entered_by_usr) > 0:
            self.ui.unlock_btn.setEnabled(True)
            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)

        else:
            self.ui.stackedWidgetmp.setCurrentWidget(self.ui.page_2)
            self.ui.unlock_btn.setDisabled(True)

    def newusr(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.newuser)
        self.ui.create_new_user_btn_10.clicked.connect(self.back1)

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

                    sqlmanagerhelper.masterpasswordsave(hasheddata)

                    self.more()

            else:
                # Pass No Match
                self.ui.substackedWidget.setCurrentWidget(self.ui.pass_no_match)

        else:
            self.ui.substackedWidget.setCurrentWidget(self.ui.page_3)

    def admin_multiple(self):

        admin_field = self.ui.admin_username.text()
        admin_field_len = len(admin_field)

        if admin_field_len > 0:
            self.ui.admin_password.setEnabled(True)
            self.ui.admin_confirm_password.setEnabled(True)

            self.ui.admin_password.textChanged.connect(self.password_ckh_admin)

        elif admin_field_len == 0:
            self.ui.admin_password.setText("")
            self.ui.admin_confirm_password.setText("")

            self.ui.admin_password.setDisabled(True)
            self.ui.admin_confirm_password.setDisabled(True)

    def passinfo2(self):
        from passwordstrengthhelper import MainWindow
        password = self.ui.admin_password.text()
        lenofpass = len(password)

        if lenofpass > 0:
            self.win = MainWindow(password, 20000000000)
            self.win.show()

    def create_admin_account(self):

        pass

    def password_ckh_admin(self):
        password = self.ui.admin_password.text()
        lenofpass = len(password)

        if lenofpass > 0:
            self.ui.admin_password.textChanged.connect(self.setpassstrenght2)
            self.ui.admin_create_account.clicked.connect(self.create_admin_account)

    def setpassstrenght2(self):
        password = self.ui.admin_password.text()
        lenofpass = len(password)

        if lenofpass > 0:
            input_string = passstrenght.passwordstrenght(password)

            if input_string == "strong":
                self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_20)
                self.ui.admin_create_account.setEnabled(True)

            elif input_string == "moderate":
                self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_19)
                self.ui.admin_create_account.setEnabled(True)
            elif input_string == "weak":
                self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_18)
                self.ui.admin_create_account.setDisabled(True)

        elif lenofpass == 0:
            self.ui.substackedWidget_3.setCurrentWidget(self.ui.page_17)
            self.ui.admin_create_account.setDisabled(True)

    def show(self):
        self.main_win.show()

    def back1(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page_7)

    def shownewusr(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.newuser)

    def showlogin(self):
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.login)

    def show_warn(self):
        self.ui.warning_encrypt.setCurrentWidget(self.ui.warn_usr)

    def show_good(self):
        self.ui.warning_encrypt.setCurrentWidget(self.ui.good)

    def warn(self, errorfilename):
        from errorhelp import MainWindow

        self.win = MainWindow(str(errorfilename))

        self.win.ui.label.setText("An Action Was Requested.")
        self.win.ui.textBrowser.setText("Are You Sure About Your Actions & Want To Continue.")
        self.win.ui.pushButton_3.clicked.connect(self.tryagain)
        self.win.ui.pushButton_2.clicked.connect(self.delete_all_files)
        self.win.show()

    def delete_all_files(self):
        from errorhelp import MainWindow
        self.win = MainWindow("")
        self.win.close()

        self.main_win.close()

        dlg = QMessageBox()
        dlg.setWindowIcon(QIcon("icons\info.svg"))
        dlg.setWindowTitle("Information")
        dlg.setText("Please Note That The Vault Has Been Reset. To "
                    "Complete The Setup Relaunch The Application. "
                    "The Application Will Exit Now...")

        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Ok:
            try:
                os.remove("usr_settings.db")

            except:
                pass
            sys.exit()

    def tryagain(self):
        self.loginusr()
        from errorhelp import MainWindow

        self.win = MainWindow("")
        self.win.close()

    def more(self):
        self.ui.warning_encrypt.setCurrentWidget(self.ui.good)
        self.ui.MainstackedWidget.setCurrentWidget(self.ui.page)

        # Show Warning If None
        self.ui.none.clicked.connect(self.show_warn)

        # Else
        self.ui.pycryptodome.clicked.connect(self.show_good)
        self.ui.pyaescrypt.clicked.connect(self.show_good)

        self.ui.confirm_encryption_type.clicked.connect(self.lastauth)

    def nonepyaesdome(self, value):
        try:
            sqlmanagerhelper.type(value)
            print(sqlmanagerhelper.dynamic_table_fetch("type", "method", "usr_settings.db"))

            self.ui.confirm_encryption_type.setDisabled(True)
            self.ui.pyaescrypt.setDisabled(True)
            self.ui.pycryptodome.setDisabled(True)
            self.ui.none.setDisabled(True)

        except Exception as error:
            self.errorui(error)

    def setpassstrenght(self):
        password = self.ui.create_single_user_password_line_1.text()
        lenofpass = len(password)

        if lenofpass > 0:
            input_string = passstrenght.passwordstrenght(password)

            if input_string == "strong":
                self.ui.substackedWidget.setCurrentWidget(self.ui.page_6)
                self.ui.create_new_user_btn.setEnabled(True)

            elif input_string == "moderate":
                self.ui.substackedWidget.setCurrentWidget(self.ui.page_5)
                self.ui.create_new_user_btn.setEnabled(True)
            elif input_string == "weak":
                self.ui.substackedWidget.setCurrentWidget(self.ui.page_4)
                self.ui.create_new_user_btn.setDisabled(True)

        elif lenofpass == 0:
            self.ui.substackedWidget.setCurrentWidget(self.ui.page_3)
            self.ui.create_new_user_btn.setDisabled(True)

    def passinfo(self):
        from passwordstrengthhelper import MainWindow
        password = self.ui.create_single_user_password_line_1.text()
        lenofpass = len(password)

        if lenofpass > 0:
            self.win = MainWindow(password, 20000000000)
            self.win.show()

    def lastauth(self):
        try:

            # Correct

            pyaescrypt = str(self.ui.pyaescrypt.isChecked())
            pycryptodome = str(self.ui.pycryptodome.isChecked())
            none = str(self.ui.none.isChecked())

            if pyaescrypt == "True":
                self.nonepyaesdome("pyaescrypt")

            if pycryptodome == "True":
                self.nonepyaesdome("pycryptodome")

            if none == "True":
                self.nonepyaesdome("none")

        except Exception as error:
            self.errorui(error)

    def errorui(self, error):
        from error import Ui_Dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)


        self.ui.textBrowser.setText(str(error))
        self.ui.pushButton_3.setText("OK")
        self.ui.pushButton_2.hide()
        self.window.setModal(True)
        self.ui.pushButton_3.clicked.connect(self.tryagain)
        self.window.show()

    def iconfix(self):
        self.main_win.setWindowIcon(QIcon("icons\Win_icon.ico"))
        self.main_win.setWindowTitle("Data Manager")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
