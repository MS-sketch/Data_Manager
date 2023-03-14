from passwordstrength import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
import sys
from PySide2 import QtCore
from PyQt5.QtGui import *

class MainWindow:
    def __init__(self, password1, crack_usr_speed):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)
        self.icon_fix()

        self.passwordinfo(password1, crack_usr_speed)

        self.main_win.setModal(True)


    def icon_fix(self):
        self.main_win.setWindowIcon(QIcon("icons\info.svg"))
        self.main_win.setWindowTitle("Password Strength Information")

    def passwordinfo(self, password1, crack_usr_speed):
        self.ui.pushButton.clicked.connect(self.winclose)

        import sys
        import re

        entropy = 0
        crack_speed = crack_usr_speed

        if len(sys.argv) > 1:
            if sys.argv[1].isdigit():
                crack_speed = int(sys.argv[1])

        policies = {'Uppercase characters': 0,
                    'Lowercase characters': 0,
                    'Special characters': 0,
                    'Numbers': 0}

        entropies = {'Uppercase characters': 26,
                    'Lowercase characters': 26,
                    'Special characters': 33,
                    'Numbers': 10}


        self.ui.textBrowser.setText("Basic Password Strength Evaluation\n")
        self.ui.textBrowser.append("Based on password cracking at: {:,d} MH/s.".format(int(crack_speed / 1000000)))
        self.ui.textBrowser.append("[Note: The Speed Is Averaged] \n")

        password = password1
        pass_len = len(password)

        for char in password:

            if re.match("[0-9]", char):
                policies["Numbers"] += 1

            elif re.match("[a-z]", char):
                policies["Lowercase characters"] += 1

            elif re.match("[A-Z]", char):
                policies["Uppercase characters"] += 1

            else:  # elif re.match("[\[\] !\"#$%&'()*+,-./:;<=>?@\\^_`{|}~]", char): # This regex can be used, but everything else should be considered special char
                policies["Special characters"] += 1

        del password  # Remove password from memory
        self.ui.textBrowser.append("\n%-25s %d\n" % ("Password length:", pass_len))


        for policy in policies.keys():

            num = policies[policy] if policies[policy] > 0 else '-'  # Handle missing policies
            self.ui.textBrowser.append("%-25s %s" % (policy + ":", str(num)))

            if policies[policy] > 0:
                entropy += entropies[policy]

        self.ui.textBrowser.append("\n%-25s %d" % ("Password entropy:", entropy))


        # Calculate the time to crack
        try:
            time_ = "hours"
            cracked = ((entropy ** pass_len) / crack_speed) / 3600  # Hours in seconds

            if cracked > 24:
                cracked = cracked / 24
                time_ = "days"

            if cracked > 365:
                cracked = cracked / 365
                time_ = "years"

            if time_ == "years" and cracked > 100:
                cracked = cracked / 100
                time_ = "centuries"

            if time_ == "centuries" and cracked > 1000:
                cracked = cracked / 1000
                time_ = "millennia"

            self.ui.textBrowser.append("\nTime to crack password:   {:,.2f} {}".format(cracked, time_))

        except Exception as error:
            self.main_win.hide()
            self.error(error)


    def error(self, error):
        error1 = str(error)
        from error import Ui_Dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)

        self.window.setWindowTitle("Data Manager Error Handler")
        self.window.setWindowIcon(QIcon("icons\loader.svg"))

        self.ui.textBrowser.setText(error1)
        self.ui.pushButton_3.setText("OK")
        self.ui.pushButton_2.hide()
        self.window.setModal(True)
        self.ui.pushButton_3.clicked.connect(self.tryagain)
        self.window.show()

    def tryagain(self):
        self.window.close()
        self.main_win.close()

    def close(self):
        self.main_win.close()

    def show(self):
        self.main_win.show()

    def winclose(self):
        self.main_win.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())