# 只是练习一下其他的如何创建一个界面
import sys
from PyQt5.QtWidgets import *

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.initUI()


    def initUI(self):
        self.resize(500,100)

        layout = QVBoxLayout()

        self.btn = QPushButton()
        self.btn.setText("Test_!")
        self.btn.clicked.connect(self.printf)
        layout.addWidget(self.btn)


        self.show1 = QLabel()
        self.show1.setText(str(self.number))
        layout.addWidget(self.show1)

        self.show2 = QLineEdit()
        self.show2.setText(str(self.number))
        layout.addWidget(self.show2)



        self.setLayout(layout)

    def  printf(self):
        print("Hello World")
        self.number =  self.number + 1
        self.show1.setText(str(self.number))
        self.show2.setText(str(self.number))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = FirstWindow()
    mainWindow.show()
    sys.exit(app.exec_())

