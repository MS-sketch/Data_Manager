from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 160)
        Dialog.setMinimumSize(QtCore.QSize(481, 160))
        Dialog.setMaximumSize(QtCore.QSize(481, 160))
        Dialog.setStyleSheet("background-color: rgb(56, 58, 89);\n"
"color: rgb(220, 220, 220);")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 51, 51))
        self.pushButton.setStyleSheet("QPushButton { \n"
"   background-color: transparent; \n"
"   border: 0px}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/construction_attention_alert_icon_153258.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 10, 481, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 55, 55)")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(70, 50, 401, 61))
        self.textBrowser.setStyleSheet("QTextBrowser { \n"
"   background-color: transparent; \n"
"   border: 0px}")
        self.textBrowser.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 120, 75, 31))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(98, 98, 98);  \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 120, 75, 31))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(98, 98, 98);  \n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "An Error Occured:"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HI</p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "OK"))
        self.pushButton_3.setText(_translate("Dialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
