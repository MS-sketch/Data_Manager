import sys
from PySide6 import QtCore
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QApplication,QMainWindow,QDialog)
from splash import Ui_MainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QIcon
from authcheck import MainWindow_auth

class authentication(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = MainWindow_auth()
        self.ui.show()


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()

    def progress(self):
        counter = 0
        while True:
            self.ui.progressBar.setValue(counter)

            if counter >=100:
                self.close()
                self.main = authentication()
                self.timer.stop()
                break

            if counter < 100:
                counter = counter + 1

    def errorui(self, errorfilename):
        text_limit = QMessageBox()
        text_limit.setWindowIcon(QIcon("icons\info.svg"))
        text_limit.setWindowTitle("Error 404 File Not Found")
        text_limit.setText("A file named '" + str(errorfilename) + "' is a critical file for the functioning of the"
                                                                   " program which is not found."
                                                                   " The program must be reinstalled.")

        text_limit.setStandardButtons(QMessageBox.StandardButton.Abort)
        text_limit.setIcon(QMessageBox.Icon.Critical)
        button = text_limit.exec()

        if button == QMessageBox.StandardButton.Abort:
            pass
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())