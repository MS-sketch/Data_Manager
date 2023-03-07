from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip, QMainWindow
import sys
import PySide2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        MainWindow.setMinimumSize(QtCore.QSize(680, 400))
        MainWindow.setMaximumSize(QtCore.QSize(680, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
"  \n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.mainappname = QtWidgets.QLabel(self.dropShadowFrame)
        self.mainappname.setGeometry(QtCore.QRect(-2, 10, 661, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.mainappname.setFont(font)
        self.mainappname.setStyleSheet("color: rgb(254, 121, 199);")
        self.mainappname.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainappname.setObjectName("mainappname")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(30, 230, 601, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"  \n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::Chunk{\n"
"   border-radius: 10px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199,       255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 9)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_2loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2loading.setGeometry(QtCore.QRect(130, 270, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label_2loading.setFont(font)
        self.label_2loading.setStyleSheet("color: rgb(161, 161, 161);")
        self.label_2loading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2loading.setObjectName("label_2loading")
        self.credit = QtWidgets.QLabel(self.dropShadowFrame)
        self.credit.setGeometry(QtCore.QRect(130, 320, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.credit.setFont(font)
        self.credit.setStyleSheet("color: rgb(161, 161, 161);")
        self.credit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.credit.setObjectName("credit")
        self.mainappname_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.mainappname_2.setGeometry(QtCore.QRect(140, 130, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.mainappname_2.setFont(font)
        self.mainappname_2.setStyleSheet("color: rgb(161, 161, 161);\n"
"")
        self.mainappname_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainappname_2.setObjectName("mainappname_2")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainappname.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:700;\">Data Manager</span></p></body></html>"))
        self.label_2loading.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Loading...</span></p></body></html>"))
        self.credit.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:700;\">By</span><span style=\" font-size:9pt;\"> Mainakh Sarkar</span></p></body></html>"))
        self.mainappname_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Loading Components...</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())
