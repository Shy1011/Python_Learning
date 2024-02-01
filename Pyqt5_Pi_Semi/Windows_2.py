from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class window_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.resize(500,500)
        # self.setGeometry(100,100,500,500)
        layout = QVBoxLayout()
        self.btn = QPushButton()
        self.btn.setText("Image 1")
        self.btn.clicked.connect(self.close)  # 这个是顺便关闭原来的窗口，
        self.btn.clicked.connect(self.changeTo2)
        self.setLayout(layout)
        layout.addWidget(self.btn)

    def changeTo2(self) :
        from Windows_1 import window_1
        win1 = window_1()
        win1.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = window_2()
    c.show()
    sys.exit(app.exec_())