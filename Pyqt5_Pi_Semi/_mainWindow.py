import sys
from mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
class MainPageWindow(Ui_MainWindow):
    def printf(self):
        print("Hello World")

    def __init__(self):
        super().__init__()
        self.pushButton_4.clicked.connect(self.printf())


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    widget = MainPageWindow()
    widget.show()
    sys.exit(app.exec_())