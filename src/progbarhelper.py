import sys
import time

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QDialog
from progbar import Ui_Dialog

class MainWindow:
    def __init__(self):
        self.main_win = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.main_win)
        self.main_win.setModal(True)
        self.show()
        self.progbar()


    def progbar(self):
        for x in range (0, 101):
            if x >= 100:
                self.close()

            else:
                self.ui.progressBar.setValue(x + 1)
                time.sleep(0.01)


    def show(self):
        self.main_win.show()

    def close(self):
        self.main_win.close()
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())