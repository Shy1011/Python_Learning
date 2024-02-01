"""
dialog对话框不能显示用于输入的控件吗?
答案 :  能

"""
import sys

from PyQt5.QtWidgets import *

Debug = 2

if Debug == 1 :
    class window(QDialog):

        def __init__(self):
            super().__init__()
            self.initUI()


        def initUI(self):
            layout = QVBoxLayout()

            self.text1 = QLineEdit()
            self.text1.setPlaceholderText("Enter text here")
            # btn = QPushButton(self)


            layout.addWidget(self.text1)

            self.setLayout(layout)

    if __name__ == "__main__" :
        app = QApplication(sys.argv)
        win = window()
        win.show()


        sys.exit(app.exec_())

elif Debug == 2 :
    class window(QDialog):

        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            layout = QVBoxLayout(self)

            self.text1 = QLineEdit()
            self.text1.setPlaceholderText("Enter text here")
            # btn = QPushButton(self)

            layout.addWidget(self.text1)

            # self.setLayout(layout)


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = window()
        win.show()

        sys.exit(app.exec_())

