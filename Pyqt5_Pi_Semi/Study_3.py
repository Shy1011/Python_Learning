"""
界面之间互相切换
实现多个界面之间互相切换
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('界面切换示例')

        self.stackedWidget = QStackedWidget(self)

        # 创建第一个界面
        self.page1 = QWidget()
        layout1 = QVBoxLayout()
        label1 = QLabel('这是第一个界面')
        button1 = QPushButton('切换到第二个界面', self)
        button1.clicked.connect(self.showPage2)

        layout1.addWidget(label1)
        layout1.addWidget(button1)
        self.page1.setLayout(layout1)

        # 创建第二个界面
        self.page2 = QWidget()
        layout2 = QVBoxLayout()
        label2 = QLabel('这是第二个界面')
        button2 = QPushButton('切换到第一个界面', self)
        button2.clicked.connect(self.showPage1)

        layout2.addWidget(label2)
        layout2.addWidget(button2)
        self.page2.setLayout(layout2)

        # 将界面添加到 QStackedWidget 中
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)

        # 设置默认显示的界面
        self.stackedWidget.setCurrentWidget(self.page1)

        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)

        self.setLayout(layout)

    def showPage1(self):
        self.stackedWidget.setCurrentWidget(self.page1)

    def showPage2(self):
        self.stackedWidget.setCurrentWidget(self.page2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
