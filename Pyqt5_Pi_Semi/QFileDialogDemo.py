'''

文件对话框：QFileDialog

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button1 = QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)
        self.setWindowTitle('文件对话框演示 ')

    def loadImage(self):
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)') # 打开了相对应的图片选项对话框
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)  # 可以选择任何文件
        dialog.setFilter(QDir.Files) # 只显示文件 不显示目录

        if dialog.exec():
            filenames = dialog.selectedFiles() # 获取用户选择的文件名，返回一个包含文件名的列表。
            f = open(filenames[0],encoding='utf-8',mode='r')
            with f:
                """
                with 语句创建了一个上下文管理器，用于对资源（例如文件、网络连接等）的获取和释放进行管理。对于文件操作，使用 with 语句可以确保在离开 with 代码块时，文件会被自动关闭。
                """
                data = f.read()
                self.contents.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())