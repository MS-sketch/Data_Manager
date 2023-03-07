"""
This Module will support & help the password generation & enable functions. It is highly recommended
not to change the code if you don't know what are you doing.
"""


import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
import random
from passwordui import Ui_Dialog
import pyperclip
import passstrenght
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow_Password:

    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)

        self.css()

        self.passwordgen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.pushButton_2.clicked.connect(self.passwordgen)


        self.ui.lineEdit.textChanged.connect(self.passwordgen)

        self.ui.pushButton_2.setIcon(QIcon("icons/refresh-cw.svg"))

        self.ui.pushButton.clicked.connect(self.copypass)

        self.ui.checkBox.clicked.connect(self.checkboxchk)
        self.ui.checkBox_2.clicked.connect(self.checkboxchk)
        self.ui.checkBox_3.clicked.connect(self.checkboxchk)
        self.ui.checkBox_4.clicked.connect(self.checkboxchk)

        self.ui.spinBox.textChanged.connect(self.passwordgen)
        self.ui.pushButton_3.clicked.connect(self.passinfo)

        self.ui.lineEdit.textChanged.connect(self.lineeditchk)




    def css(self):
        self.main_win.setWindowIcon(QIcon("icons\Win_icon.ico"))
        self.main_win.setWindowTitle("Password Generator")


    def lineeditchk(self):
        lineeditlen = self.ui.lineEdit.text()

        #validator = QRegularExpressionValidator(QRegularExpression("[0-9_]+"))

        #self.ui.lineEdit.setValidator(validator)

    def passinfo(self):
        from passwordstrengthhelper import MainWindow
        password = self.ui.label_9.text()
        lenofpass = len(password)

        if lenofpass > 0:
            self.win = MainWindow(password, 20000000000) #defaut value
            self.win.show()

        else:
            error = QMessageBox()
            error.setWindowIcon(QIcon("icons\info.svg"))
            error.setWindowTitle("Information")
            error.setText("Sorry, but it appears that the password you have entered is of '" + str(lenofpass) +
                          "' length which is not a valid whole number. \n"
                          "If you encounter this problem repeatedly then please reinstall the application.")

            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error.setIcon(QMessageBox.Icon.Critical)
            button = error.exec()

    def show(self):
        self.main_win.show()

    def close(self):
        self.main_win.close()

    def passwordgen(self):
        self.ui.pushButton.setText("Copy")
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

                input_string = passstrenght.passwordstrenght(password)


                if input_string == "strong":
                    self.ui.weakpass.setCurrentWidget(self.ui.strong)

                elif input_string == "moderate":
                    self.ui.weakpass.setCurrentWidget(self.ui.moderate)
                elif input_string == "weak":
                    self.ui.weakpass.setCurrentWidget(self.ui.weak)

    def copypass(self):
        password = self.ui.label_9.text()
        pyperclip.copy(password)
        self.ui.pushButton.setText("Copied!")


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
    main_win = MainWindow_Password()
    main_win.show()
    sys.exit(app.exec())