"""This Module will support & help the password generation & enable functions. It is highly recommended
not to change the code if you don't know what are you doing..."""

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog
import time
import random
from passwordui import Ui_Dialog
import pyperclip

class MainWindow:

    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)
        self.passwordgen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.pushButton_2.clicked.connect(self.passwordgen)

        self.ui.pushButton.clicked.connect(self.copypass)

        self.ui.checkBox.clicked.connect(self.checkboxchk)
        self.ui.checkBox_2.clicked.connect(self.checkboxchk)
        self.ui.checkBox_3.clicked.connect(self.checkboxchk)
        self.ui.checkBox_4.clicked.connect(self.checkboxchk)




    def show(self):
        self.main_win.show()

    def passwordgen(self):
        checked1 = str(self.ui.checkBox.isChecked())
        checked2 = str(self.ui.checkBox_2.isChecked())
        checked3 = str(self.ui.checkBox_3.isChecked())
        checked4 = str(self.ui.checkBox_4.isChecked())

        checkboxchars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        checkboxchars2 = "abcdefghijklmnopqrstuvwxyz"
        checkboxchars3 = "1234567890"
        checkboxchars4 = self.ui.lineEdit.text()

        pass_len = int(self.ui.spinBox.value())

        for x in range(0, 1):
            chars = ""
            if checked1 == "True":
                chars = checkboxchars1 + chars

            if checked2 == "True":
                chars = checkboxchars2 + chars

            if checked3 == "True":
                chars = checkboxchars3 + chars


            if checked4 == "True":
                if len(checkboxchars4) == 0:
                    defaultconfig = "~!@#$%^&*+-/.,\{}[]();:|?<>='`" + '"'
                    self.ui.lineEdit.setText(defaultconfig)
                    chars = defaultconfig + chars


                else:
                    correct = str(checkboxchars4.isspace())
                    if correct == "True":
                        defaultconfig2 = "~!@#$%^&*+-/.,\{}[]();:|?<>='`" + '"'
                        self.ui.lineEdit.setText(defaultconfig2)
                        chars = defaultconfig2 + chars
                    else:
                        chars = checkboxchars4 + chars





            for x in range(0, 1):
                password = ""
                for x in range(0, pass_len):
                    pass_char = random.choice(chars)
                    password = password + pass_char

                if len(str(password)) > 25:
                    compressed = password[0:25] + ("...")
                    self.ui.label_5.setText(compressed)
                    self.ui.label_9.setText(password)

                else:
                    self.ui.label_5.setText(password)
                    self.ui.label_9.setText(password)

                input_string = password

                n = len(input_string)

                hasLower = False
                hasUpper = False
                hasDigit = False
                specialChar = False
                normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

                for i in range(n):
                    if input_string[i].islower():
                        hasLower = True
                    if input_string[i].isupper():
                        hasUpper = True
                    if input_string[i].isdigit():
                        hasDigit = True
                    if input_string[i] not in normalChars:
                        specialChar = True

                # Strength of password
                if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
                    self.ui.weakpass.setCurrentWidget(self.ui.strong)

                elif ((hasLower or hasUpper) and specialChar and n >= 6):
                    self.ui.weakpass.setCurrentWidget(self.ui.moderate)
                else:
                    self.ui.weakpass.setCurrentWidget(self.ui.weak)

    def copypass(self):
        password = self.ui.label_9.text()
        pyperclip.copy(password)




    def checkboxchk(self):
        checked1 = str(self.ui.checkBox.isChecked())
        checked2 = str(self.ui.checkBox_2.isChecked())
        checked3 = str(self.ui.checkBox_3.isChecked())
        checked4 = str(self.ui.checkBox_4.isChecked())
        if checked1 == "False" and checked2 == "False" and checked3 == "False" and checked4 == "False":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
            self.ui.spinBox.setDisabled(True)


        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            self.ui.spinBox.setEnabled(True)
            self.passwordgen()

    def error(self, error):
        from error import Ui_Dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.ui.textBrowser.setText(error)
        self.ui.pushButton_3.setText("OK")
        self.ui.pushButton_2.hide()
        self.window.setModal(True)
        self.ui.pushButton_3.clicked.connect(self.tryagain)
        self.window.show()

    def tryagain(self):
        self.window.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())