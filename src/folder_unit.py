from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(988, 568)
        Dialog.setMinimumSize(QtCore.QSize(988, 568))
        Dialog.setMaximumSize(QtCore.QSize(988, 568))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(507, 0, 211, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(397, 60, 561, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.create_folder_2 = QtWidgets.QPushButton(self.page)
        self.create_folder_2.setGeometry(QtCore.QRect(250, 230, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_folder_2.setFont(font)
        self.create_folder_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.create_folder_2.setToolTip("Create New Folder")
        self.create_folder_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.create_folder_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Data Manager/Project MEW/GUI INTERFACE/icons/plus-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.create_folder_2.setIcon(icon)
        self.create_folder_2.setIconSize(QtCore.QSize(24, 24))
        self.create_folder_2.setObjectName("create_folder_2")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(250, 320, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setGeometry(QtCore.QRect(125, 320, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.passwordgen_2 = QtWidgets.QPushButton(self.page)
        self.passwordgen_2.setGeometry(QtCore.QRect(370, 230, 81, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordgen_2.sizePolicy().hasHeightForWidth())
        self.passwordgen_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordgen_2.setFont(font)
        self.passwordgen_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.passwordgen_2.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.passwordgen_2.setAcceptDrops(False)
        self.passwordgen_2.setToolTip("Generate Passwords")
        self.passwordgen_2.setToolTipDuration(-1)
        self.passwordgen_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.passwordgen_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/key.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.passwordgen_2.setIcon(icon1)
        self.passwordgen_2.setIconSize(QtCore.QSize(24, 24))
        self.passwordgen_2.setObjectName("passwordgen_2")
        self.create_entry_2 = QtWidgets.QPushButton(self.page)
        self.create_entry_2.setGeometry(QtCore.QRect(130, 230, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_entry_2.setFont(font)
        self.create_entry_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.create_entry_2.setToolTip("Create New Entry")
        self.create_entry_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.create_entry_2.setText("")
        self.create_entry_2.setIcon(icon)
        self.create_entry_2.setIconSize(QtCore.QSize(24, 24))
        self.create_entry_2.setObjectName("create_entry_2")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(350, 320, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.page)
        self.label_8.setGeometry(QtCore.QRect(120, 170, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 20, 531, 431))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 529, 429))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(9, 36, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setGeometry(QtCore.QRect(9, 111, 62, 16))
        self.label_10.setObjectName("label_10")
        self.web_address = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.web_address.setGeometry(QtCore.QRect(9, 58, 471, 21))
        self.web_address.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhUrlCharactersOnly)
        self.web_address.setObjectName("web_address")
        self.primary_websitedomain = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.primary_websitedomain.setGeometry(QtCore.QRect(9, 85, 243, 20))
        self.primary_websitedomain.setChecked(True)
        self.primary_websitedomain.setObjectName("primary_websitedomain")
        self.user_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.user_name.setGeometry(QtCore.QRect(9, 133, 471, 21))
        self.user_name.setObjectName("user_name")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 9, 281, 21))
        self.lineEdit_2.setAccessibleName("")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setGeometry(QtCore.QRect(9, 160, 53, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(9, 182, 441, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.notes = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.notes.setGeometry(QtCore.QRect(9, 231, 471, 101))
        self.notes.setObjectName("notes")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setGeometry(QtCore.QRect(9, 209, 34, 16))
        self.label_12.setObjectName("label_12")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(460, 170, 31, 41))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.pushButton = QtWidgets.QPushButton(self.page_8)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 31, 24))
        self.pushButton.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_9)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 10, 31, 24))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget_2.addWidget(self.page_9)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_3.setGeometry(QtCore.QRect(10, 370, 511, 51))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.new_save = QtWidgets.QWidget()
        self.new_save.setObjectName("new_save")
        self.discard = QtWidgets.QPushButton(self.new_save)
        self.discard.setGeometry(QtCore.QRect(330, 10, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discard.sizePolicy().hasHeightForWidth())
        self.discard.setSizePolicy(sizePolicy)
        self.discard.setMaximumSize(QtCore.QSize(100, 16777215))
        self.discard.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.discard.setObjectName("discard")
        self.reset = QtWidgets.QPushButton(self.new_save)
        self.reset.setGeometry(QtCore.QRect(432, 10, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reset.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.reset.setObjectName("reset")
        self.comboBox = QtWidgets.QComboBox(self.new_save)
        self.comboBox.setGeometry(QtCore.QRect(174, 12, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_20 = QtWidgets.QLabel(self.new_save)
        self.label_20.setGeometry(QtCore.QRect(104, 17, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.save_btn_6 = QtWidgets.QPushButton(self.new_save)
        self.save_btn_6.setGeometry(QtCore.QRect(20, 10, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn_6.sizePolicy().hasHeightForWidth())
        self.save_btn_6.setSizePolicy(sizePolicy)
        self.save_btn_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.save_btn_6.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.save_btn_6.setObjectName("save_btn_6")
        self.stackedWidget_3.addWidget(self.new_save)
        self.edit_save = QtWidgets.QWidget()
        self.edit_save.setObjectName("edit_save")
        self.reset_2 = QtWidgets.QPushButton(self.edit_save)
        self.reset_2.setGeometry(QtCore.QRect(431, 10, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_2.sizePolicy().hasHeightForWidth())
        self.reset_2.setSizePolicy(sizePolicy)
        self.reset_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reset_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.reset_2.setObjectName("reset_2")
        self.discard_2 = QtWidgets.QPushButton(self.edit_save)
        self.discard_2.setGeometry(QtCore.QRect(331, 10, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discard_2.sizePolicy().hasHeightForWidth())
        self.discard_2.setSizePolicy(sizePolicy)
        self.discard_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.discard_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.discard_2.setObjectName("discard_2")
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.edit_save)
        self.stackedWidget_4.setGeometry(QtCore.QRect(19, 4, 301, 31))
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_15 = QtWidgets.QLabel(self.page_10)
        self.label_15.setGeometry(QtCore.QRect(86, 13, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.save_btn_2 = QtWidgets.QPushButton(self.page_10)
        self.save_btn_2.setGeometry(QtCore.QRect(2, 6, 75, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn_2.sizePolicy().hasHeightForWidth())
        self.save_btn_2.setSizePolicy(sizePolicy)
        self.save_btn_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.save_btn_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.save_btn_2.setObjectName("save_btn_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_10)
        self.comboBox_2.setGeometry(QtCore.QRect(157, 8, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.stackedWidget_4.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.save_btn_3 = QtWidgets.QPushButton(self.page_11)
        self.save_btn_3.setGeometry(QtCore.QRect(210, 6, 81, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn_3.sizePolicy().hasHeightForWidth())
        self.save_btn_3.setSizePolicy(sizePolicy)
        self.save_btn_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.save_btn_3.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 12px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.save_btn_3.setObjectName("save_btn_3")
        self.stackedWidget_4.addWidget(self.page_11)
        self.stackedWidget_3.addWidget(self.edit_save)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_2)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(99, 60, 20, 451))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 50, 110, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(-9, 58, 20, 451))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 500, 108, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.stackedWidget_search = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_search.setGeometry(QtCore.QRect(500, 0, 191, 51))
        self.stackedWidget_search.setObjectName("stackedWidget_search")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.lineEdit = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 171, 21))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.stackedWidget_search.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_search.addWidget(self.page_7)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.vault_2 = QtWidgets.QPushButton(self.frame)
        self.vault_2.setGeometry(QtCore.QRect(20, 150, 61, 41))
        self.vault_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vault_2.setFont(font)
        self.vault_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.vault_2.setToolTip("Shows All Stored Data")
        self.vault_2.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.vault_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/database.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.vault_2.setIcon(icon2)
        self.vault_2.setIconSize(QtCore.QSize(24, 24))
        self.vault_2.setObjectName("vault_2")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(30, 320, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.passwordgen = QtWidgets.QPushButton(self.frame)
        self.passwordgen.setGeometry(QtCore.QRect(20, 250, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordgen.sizePolicy().hasHeightForWidth())
        self.passwordgen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordgen.setFont(font)
        self.passwordgen.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.passwordgen.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.passwordgen.setAcceptDrops(False)
        self.passwordgen.setToolTip("Generate Passwords")
        self.passwordgen.setToolTipDuration(-1)
        self.passwordgen.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.passwordgen.setText("")
        self.passwordgen.setIcon(icon1)
        self.passwordgen.setIconSize(QtCore.QSize(24, 24))
        self.passwordgen.setObjectName("passwordgen")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.main = QtWidgets.QPushButton(self.frame)
        self.main.setGeometry(QtCore.QRect(20, 100, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main.setFont(font)
        self.main.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.main.setToolTip("Open Main")
        self.main.setToolTipDuration(-1)
        self.main.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.main.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.main.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.main.setIcon(icon3)
        self.main.setIconSize(QtCore.QSize(24, 24))
        self.main.setObjectName("main")
        self.create_folder = QtWidgets.QPushButton(self.frame)
        self.create_folder.setGeometry(QtCore.QRect(60, 350, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_folder.setFont(font)
        self.create_folder.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.create_folder.setToolTip("Create New Folder")
        self.create_folder.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.create_folder.setText("")
        self.create_folder.setIcon(icon)
        self.create_folder.setIconSize(QtCore.QSize(24, 24))
        self.create_folder.setObjectName("create_folder")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.create_entry = QtWidgets.QPushButton(self.frame)
        self.create_entry.setGeometry(QtCore.QRect(10, 350, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_entry.setFont(font)
        self.create_entry.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.create_entry.setToolTip("Create New Entry")
        self.create_entry.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.create_entry.setText("")
        self.create_entry.setIcon(icon)
        self.create_entry.setIconSize(QtCore.QSize(24, 24))
        self.create_entry.setObjectName("create_entry")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 410, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.about = QtWidgets.QPushButton(self.frame)
        self.about.setGeometry(QtCore.QRect(20, 440, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.about.setFont(font)
        self.about.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.about.setToolTip("About")
        self.about.setStyleSheet("QPushButton{\n"
"  border: 1.5px solid black;\n"
"  border-radius: 15px;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(213, 213, 213);  \n"
"}")
        self.about.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.about.setIcon(icon4)
        self.about.setIconSize(QtCore.QSize(24, 24))
        self.about.setObjectName("about")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(130, 54, 261, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.Entries = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Entries.sizePolicy().hasHeightForWidth())
        self.Entries.setSizePolicy(sizePolicy)
        self.Entries.setObjectName("Entries")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.Entries)
        self.scrollArea_3.setGeometry(QtCore.QRect(-3, 2, 261, 431))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 259, 429))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.Entries, "")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_search.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.create_folder_2.setStatusTip(_translate("Dialog", "Create New Folder"))
        self.label_17.setText(_translate("Dialog", "New Folder"))
        self.label_16.setText(_translate("Dialog", "New Entry"))
        self.passwordgen_2.setStatusTip(_translate("Dialog", "Generate New Password"))
        self.passwordgen_2.setWhatsThis(_translate("Dialog", "Generate Passwords"))
        self.passwordgen_2.setAccessibleName(_translate("Dialog", "Generate Passwords"))
        self.passwordgen_2.setAccessibleDescription(_translate("Dialog", "Generate Passwords"))
        self.create_entry_2.setStatusTip(_translate("Dialog", "Create New Entry"))
        self.label_18.setText(_translate("Dialog", "Generate Password"))
        self.label_8.setText(_translate("Dialog", "Nothing Here, Create Something New?"))
        self.label_9.setText(_translate("Dialog", "Website Address:"))
        self.label_10.setText(_translate("Dialog", "User Name:"))
        self.primary_websitedomain.setText(_translate("Dialog", "Use this address as Primary Host Address."))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Title"))
        self.label_11.setText(_translate("Dialog", "Password:"))
        self.label_12.setText(_translate("Dialog", "Notes:"))
        self.pushButton.setText(_translate("Dialog", "S"))
        self.pushButton_2.setText(_translate("Dialog", "H"))
        self.discard.setText(_translate("Dialog", "Discard"))
        self.reset.setText(_translate("Dialog", "Reset All"))
        self.comboBox.setItemText(0, _translate("Dialog", "No Folder"))
        self.comboBox.setItemText(1, _translate("Dialog", "Create A New Folder"))
        self.label_20.setText(_translate("Dialog", "To Folder"))
        self.save_btn_6.setText(_translate("Dialog", "Save"))
        self.reset_2.setText(_translate("Dialog", "Close"))
        self.discard_2.setText(_translate("Dialog", "Delete"))
        self.label_15.setText(_translate("Dialog", "To Folder"))
        self.save_btn_2.setText(_translate("Dialog", "Save"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "No Folder"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Create A New Folder"))
        self.save_btn_3.setText(_translate("Dialog", "Edit"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Search Through You Entries"))
        self.label.setText(_translate("Dialog", "Folder Name"))
        self.vault_2.setStatusTip(_translate("Dialog", "Open All Your Stored Data"))
        self.label_13.setText(_translate("Dialog", "Create"))
        self.passwordgen.setStatusTip(_translate("Dialog", "Generate New Password"))
        self.passwordgen.setWhatsThis(_translate("Dialog", "Generate Passwords"))
        self.passwordgen.setAccessibleName(_translate("Dialog", "Generate Passwords"))
        self.passwordgen.setAccessibleDescription(_translate("Dialog", "Generate Passwords"))
        self.label_2.setText(_translate("Dialog", "New Entry"))
        self.main.setStatusTip(_translate("Dialog", "Open The Main Menu"))
        self.create_folder.setStatusTip(_translate("Dialog", "Create New Folder"))
        self.label_3.setText(_translate("Dialog", "All Entries"))
        self.create_entry.setStatusTip(_translate("Dialog", "Create New Entry"))
        self.label_4.setText(_translate("Dialog", "More"))
        self.about.setStatusTip(_translate("Dialog", "About Data Manager"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Entries), _translate("Dialog", "Entries"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
