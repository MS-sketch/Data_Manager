import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QIcon
from about import Ui_About

class MainWindow_About:
    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_About()
        self.ui.setupUi(self.main_win)

        self.css()

        #Default Config
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.stackedWidget_upd.setCurrentWidget(self.ui.app_ver)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.tabWidget_2.setCurrentIndex(0)



        #Software Update
        self.ui.pushButton_6.clicked.connect(self.openupd)

        #Updating
        self.ui.pushButton_9.clicked.connect(self.changewidget1)

        #Abort
        self.ui.pushButton_8.clicked.connect(self.changewidget2)


        #App Info
        self.ui.pushButton_5.clicked.connect(self.openappver)



    def css(self):
        self.main_win.setWindowIcon(QIcon("icons\Win_icon.ico"))
        self.main_win.setWindowTitle("About Data Manager")
        self.ui.label_12.setText("Current Version \n  \n         1.2")



    def close(self):
        self.main_win.close()

    def show(self):
        self.main_win.show()

    def openupd(self):
        self.ui.stackedWidget_upd.setCurrentWidget(self.ui.soft_upd)

    def openappver(self):
        self.ui.stackedWidget_upd.setCurrentWidget(self.ui.app_ver)


    def changewidget1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def changewidget2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow_About()
    main_win.show()
    sys.exit(app.exec())