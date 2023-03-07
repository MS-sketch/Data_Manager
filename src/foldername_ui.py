from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 168)
        Dialog.setMinimumSize(QtCore.QSize(518, 168))
        Dialog.setMaximumSize(QtCore.QSize(518, 168))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, -20, 521, 221))
        self.frame.setMinimumSize(QtCore.QSize(521, 221))
        self.frame.setMaximumSize(QtCore.QSize(521, 221))
        self.frame.setStyleSheet("QFrame{\n"
"  \n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ok_btn = QtWidgets.QPushButton(self.frame)
        self.ok_btn.setGeometry(QtCore.QRect(340, 150, 75, 24))
        self.ok_btn.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255,255,255)\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.frame)
        self.cancel_btn.setGeometry(QtCore.QRect(420, 150, 75, 24))
        self.cancel_btn.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255,255,255)\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 90, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-radius: 12px")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Folder Name:"))
        self.ok_btn.setText(_translate("Dialog", "Create"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Create New Folder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
