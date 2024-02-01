from PyQt5.QtWidgets import *
import sys
from TabView import Ui_MainWindow
class Tabview(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setupUi(self)




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = Tabview()
    win.show()
    sys.exit(app.exec_())
