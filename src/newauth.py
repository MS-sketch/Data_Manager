from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 239)
        Dialog.setMinimumSize(QtCore.QSize(539, 239))
        Dialog.setMaximumSize(QtCore.QSize(539, 239))
        Dialog.setStyleSheet("")
        self.MainstackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.MainstackedWidget.setGeometry(QtCore.QRect(-1, 40, 541, 191))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MainstackedWidget.setFont(font)
        self.MainstackedWidget.setStyleSheet("background-color: rgb(56, 58, 89);\n"
"\n"
"\n"
"")
        self.MainstackedWidget.setObjectName("MainstackedWidget")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.unlock_btn = QtWidgets.QPushButton(self.login)
        self.unlock_btn.setEnabled(True)
        self.unlock_btn.setGeometry(QtCore.QRect(240, 130, 75, 24))
        self.unlock_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.unlock_btn.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.unlock_btn.setObjectName("unlock_btn")
        self.label_3 = QtWidgets.QLabel(self.login)
        self.label_3.setGeometry(QtCore.QRect(0, 30, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.master_password_single_user = QtWidgets.QLineEdit(self.login)
        self.master_password_single_user.setGeometry(QtCore.QRect(150, 70, 241, 21))
        self.master_password_single_user.setStyleSheet("QLineEdit{\n"
"color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.master_password_single_user.setText("")
        self.master_password_single_user.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.master_password_single_user.setClearButtonEnabled(False)
        self.master_password_single_user.setObjectName("master_password_single_user")
        self.forgot_password = QtWidgets.QPushButton(self.login)
        self.forgot_password.setEnabled(True)
        self.forgot_password.setGeometry(QtCore.QRect(200, 160, 161, 31))
        self.forgot_password.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.forgot_password.setStyleSheet("QPushButton{\n"
"  border: none;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.forgot_password.setObjectName("forgot_password")
        self.stackedWidgetmp = QtWidgets.QStackedWidget(self.login)
        self.stackedWidgetmp.setGeometry(QtCore.QRect(150, 90, 241, 31))
        self.stackedWidgetmp.setObjectName("stackedWidgetmp")
        self.wrongpass_enter = QtWidgets.QWidget()
        self.wrongpass_enter.setObjectName("wrongpass_enter")
        self.label_8 = QtWidgets.QLabel(self.wrongpass_enter)
        self.label_8.setGeometry(QtCore.QRect(80, 10, 141, 16))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0)\n"
"")
        self.label_8.setObjectName("label_8")
        self.stackedWidgetmp.addWidget(self.wrongpass_enter)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidgetmp.addWidget(self.page_2)
        self.MainstackedWidget.addWidget(self.login)
        self.newuser = QtWidgets.QWidget()
        self.newuser.setObjectName("newuser")
        self.label_5 = QtWidgets.QLabel(self.newuser)
        self.label_5.setGeometry(QtCore.QRect(120, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.newuser)
        self.label_6.setGeometry(QtCore.QRect(60, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.create_single_user_password_line_1 = QtWidgets.QLineEdit(self.newuser)
        self.create_single_user_password_line_1.setGeometry(QtCore.QRect(210, 60, 211, 21))
        self.create_single_user_password_line_1.setStyleSheet("color: rgb(255, 255, 255)")
        self.create_single_user_password_line_1.setText("")
        self.create_single_user_password_line_1.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.create_single_user_password_line_1.setClearButtonEnabled(True)
        self.create_single_user_password_line_1.setObjectName("create_single_user_password_line_1")
        self.create_single_user_password_confirm = QtWidgets.QLineEdit(self.newuser)
        self.create_single_user_password_confirm.setEnabled(True)
        self.create_single_user_password_confirm.setGeometry(QtCore.QRect(210, 90, 211, 21))
        self.create_single_user_password_confirm.setStyleSheet("color: rgb(255, 255, 255)")
        self.create_single_user_password_confirm.setText("")
        self.create_single_user_password_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.create_single_user_password_confirm.setClearButtonEnabled(True)
        self.create_single_user_password_confirm.setObjectName("create_single_user_password_confirm")
        self.create_new_user_btn = QtWidgets.QPushButton(self.newuser)
        self.create_new_user_btn.setEnabled(True)
        self.create_new_user_btn.setGeometry(QtCore.QRect(220, 160, 111, 24))
        self.create_new_user_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.create_new_user_btn.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.create_new_user_btn.setObjectName("create_new_user_btn")
        self.label_7 = QtWidgets.QLabel(self.newuser)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 541, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.substackedWidget = QtWidgets.QStackedWidget(self.newuser)
        self.substackedWidget.setGeometry(QtCore.QRect(180, 120, 211, 31))
        self.substackedWidget.setObjectName("substackedWidget")
        self.pass_no_match = QtWidgets.QWidget()
        self.pass_no_match.setObjectName("pass_no_match")
        self.label_2 = QtWidgets.QLabel(self.pass_no_match)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 161, 16))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_2.setObjectName("label_2")
        self.substackedWidget.addWidget(self.pass_no_match)
        self.blank_feild = QtWidgets.QWidget()
        self.blank_feild.setObjectName("blank_feild")
        self.label_4 = QtWidgets.QLabel(self.blank_feild)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 161, 16))
        self.label_4.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.substackedWidget.addWidget(self.blank_feild)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.substackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label_14.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_14.setObjectName("label_14")
        self.substackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_15 = QtWidgets.QLabel(self.page_5)
        self.label_15.setGeometry(QtCore.QRect(30, 10, 131, 16))
        self.label_15.setStyleSheet("color: rgb(0, 85, 255)")
        self.label_15.setObjectName("label_15")
        self.substackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_16 = QtWidgets.QLabel(self.page_6)
        self.label_16.setGeometry(QtCore.QRect(30, 10, 111, 16))
        self.label_16.setStyleSheet("color: rgb(0, 170, 0)")
        self.label_16.setObjectName("label_16")
        self.substackedWidget.addWidget(self.page_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.newuser)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 60, 91, 24))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainstackedWidget.addWidget(self.newuser)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(90, 10, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.confirm_encryption_type = QtWidgets.QPushButton(self.page)
        self.confirm_encryption_type.setGeometry(QtCore.QRect(450, 160, 75, 24))
        self.confirm_encryption_type.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(199, 199, 199);  \n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.confirm_encryption_type.setObjectName("confirm_encryption_type")
        self.pyaescrypt = QtWidgets.QRadioButton(self.page)
        self.pyaescrypt.setGeometry(QtCore.QRect(30, 50, 89, 20))
        self.pyaescrypt.setStyleSheet("color: rgb(255, 255, 255)")
        self.pyaescrypt.setObjectName("pyaescrypt")
        self.pycryptodome = QtWidgets.QRadioButton(self.page)
        self.pycryptodome.setGeometry(QtCore.QRect(190, 50, 151, 20))
        self.pycryptodome.setStyleSheet("color: rgb(255, 255, 255)")
        self.pycryptodome.setChecked(True)
        self.pycryptodome.setObjectName("pycryptodome")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(30, 160, 411, 20))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.none = QtWidgets.QRadioButton(self.page)
        self.none.setGeometry(QtCore.QRect(420, 50, 89, 20))
        self.none.setStyleSheet("color: rgb(255, 255, 255)")
        self.none.setObjectName("none")
        self.warning_encrypt = QtWidgets.QStackedWidget(self.page)
        self.warning_encrypt.setGeometry(QtCore.QRect(20, 70, 501, 80))
        self.warning_encrypt.setObjectName("warning_encrypt")
        self.warn_usr = QtWidgets.QWidget()
        self.warn_usr.setObjectName("warn_usr")
        self.label_13 = QtWidgets.QLabel(self.warn_usr)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 481, 51))
        self.label_13.setStyleSheet("color: rgb(255, 0, 0)")
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.warning_encrypt.addWidget(self.warn_usr)
        self.good = QtWidgets.QWidget()
        self.good.setObjectName("good")
        self.warning_encrypt.addWidget(self.good)
        self.MainstackedWidget.addWidget(self.page)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.create_new_user_btn_7 = QtWidgets.QPushButton(self.page_7)
        self.create_new_user_btn_7.setEnabled(True)
        self.create_new_user_btn_7.setGeometry(QtCore.QRect(160, 160, 111, 24))
        self.create_new_user_btn_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.create_new_user_btn_7.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  color: rgb(255, 0, 0)\n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.create_new_user_btn_7.setObjectName("create_new_user_btn_7")
        self.create_new_user_btn_8 = QtWidgets.QPushButton(self.page_7)
        self.create_new_user_btn_8.setEnabled(True)
        self.create_new_user_btn_8.setGeometry(QtCore.QRect(280, 160, 111, 24))
        self.create_new_user_btn_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.create_new_user_btn_8.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid white;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"  color: rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"  color: rgb(0, 255, 0)\n"
"}\n"
"QPushButton:disabled{\n"
"  color: rgb(199, 199, 199);  \n"
"}")
        self.create_new_user_btn_8.setObjectName("create_new_user_btn_8")
        self.label_52 = QtWidgets.QLabel(self.page_7)
        self.label_52.setGeometry(QtCore.QRect(30, 10, 501, 121))
        self.label_52.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_52.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_52.setObjectName("label_52")
        self.MainstackedWidget.addWidget(self.page_7)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-71, 0, 621, 241))
        self.frame.setStyleSheet("QFrame{\n"
"  \n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(240, 0, 201, 41))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label = QtWidgets.QLabel(self.page_23)
        self.label.setGeometry(QtCore.QRect(-10, -10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.label_51 = QtWidgets.QLabel(self.page_24)
        self.label_51.setGeometry(QtCore.QRect(-10, -10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_51.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.stackedWidget.addWidget(self.page_24)
        self.frame.raise_()
        self.MainstackedWidget.raise_()

        self.retranslateUi(Dialog)
        self.MainstackedWidget.setCurrentIndex(3)
        self.stackedWidgetmp.setCurrentIndex(1)
        self.substackedWidget.setCurrentIndex(2)
        self.warning_encrypt.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.unlock_btn.setText(_translate("Dialog", "Unlock"))
        self.label_3.setText(_translate("Dialog", "Enter Master Password To Continue"))
        self.forgot_password.setText(_translate("Dialog", "Forgot Your Main Password?"))
        self.label_8.setText(_translate("Dialog", "Wrong Password!"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.label_6.setText(_translate("Dialog", "Confirm Password:"))
        self.create_new_user_btn.setText(_translate("Dialog", "Create New Vault"))
        self.label_7.setText(_translate("Dialog", "To Create A New Vault Enter The Master Password"))
        self.label_2.setText(_translate("Dialog", "Your Passwords Don\'t Match"))
        self.label_4.setText(_translate("Dialog", "Please Enter Your Password"))
        self.label_14.setText(_translate("Dialog", "Password Is Weak"))
        self.label_15.setText(_translate("Dialog", "Password Is Moderate"))
        self.label_16.setText(_translate("Dialog", "Password Is Strong"))
        self.pushButton_2.setText(_translate("Dialog", "Password Info"))
        self.label_11.setText(_translate("Dialog", "Please Select You Preferred Method For Encryption"))
        self.confirm_encryption_type.setText(_translate("Dialog", "Ok"))
        self.pyaescrypt.setText(_translate("Dialog", "PyAesCrypt"))
        self.pycryptodome.setText(_translate("Dialog", "PyCryptoDome [Default]"))
        self.label_12.setText(_translate("Dialog", "Note: This Cannot Be Changed Later. To Change You Have To Reset The Vault"))
        self.none.setText(_translate("Dialog", "None"))
        self.label_13.setText(_translate("Dialog", "Anyone Can Access Your Data Without Your Consent. The Vault Will Just Be Hidden Under Your Master Password."))
        self.create_new_user_btn_7.setText(_translate("Dialog", "Yes"))
        self.create_new_user_btn_8.setText(_translate("Dialog", "No"))
        self.label_52.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Do You Want To Reset Your Vault?</span></p><p><br/></p><p align=\"center\"><span style=\" font-size:14pt; color:#ff0000;\">Note: Resetting Will Delete Your Old Data.</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Good Morning!"))
        self.label_51.setText(_translate("Dialog", "Good Evening!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
