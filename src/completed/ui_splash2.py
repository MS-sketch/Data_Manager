"""Component of the UI file & checks the existence of all the components required & starts the application."""

import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,QDialog,
                               QProgressBar, QSizePolicy, QVBoxLayout, QWidget, QGraphicsDropShadowEffect)

import existance
from splash import Ui_MainWindow
import linecache
import os
import time

counter = 0
from backend import items_check
from authsupporter import MainWindow

class authentication(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = MainWindow()
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
        for x in range(0, 1):
            counter = 0
            for x in range(0, 100):
                time.sleep(0.02)
                self.ui.progressBar.setValue(counter)

                if counter >= 100:
                    self.close()
                    self.main = authentication()
                    self.timer.stop()
                    break

                if counter < 100:
                    total_items = len(items_check)

                    for x in range(0, total_items):
                        if existance.exists(items_check[x]) == "TRUE":
                            counter = counter + round(100 / total_items)

                        if existance.exists(items_check[x]) == "FALSE":
                            self.close()
                            self.timer.stop()
                            
                            self.errorui(items_check[x])

                            break




    def errorui(self, errorfilename):
        from errorhelp import MainWindow

        self.win = MainWindow('"' + str(errorfilename) + '"' + " not found. Please repair or reinstall the program.")
        self.win.ui.pushButton_3.setText("OK")
        self.win.ui.pushButton_2.hide()

        #idk
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.win.ui.label.setText("Error 404 Not Found")
        self.win.ui.pushButton_3.clicked.connect(self.tryagain)
        self.win.show()

    def tryagain(self):
        sys.exit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())

