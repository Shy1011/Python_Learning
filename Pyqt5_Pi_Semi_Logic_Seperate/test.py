import sys
import dialog
from PyQt5.QtWidgets import QApplication, QMainWindow


class Mainwin(QMainWindow,dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.printf)

    def printf(self):
        print("Hello World")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Mainwin()
    ui.show()
    sys.exit(app.exec_())