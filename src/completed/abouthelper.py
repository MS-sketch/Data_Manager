import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtWidgets import QDialog
import os

from about import Ui_About


class MainWindow:
    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_About()
        self.ui.setupUi(self.main_win)

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



        #




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
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())