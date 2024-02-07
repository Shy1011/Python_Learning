"""
这个是Pi_Semi仿真测试
"""
from PyQt5.QtWidgets import *
from untitled import Ui_Form
import sys
from PyQt5 import QtCore

class win(Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = win()
    demo.show()
    sys.exit(app.exec_())