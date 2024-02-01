import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和大小
        self.setWindowTitle("Qt5 Example")
        self.setGeometry(100, 100, 400, 200)

        # 创建按钮并设置文本
        self.button = QPushButton("打开百度", self)

        # 连接按钮的点击事件到自定义的槽函数
        self.button.clicked.connect(self.openBaidu)

    def openBaidu(self):
        # 使用Qt的QDesktopServices打开浏览器并跳转到百度网址
        QDesktopServices.openUrl(QUrl("https://www.baidu.com"))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建窗口实例
    window = MyWindow()

    # 显示窗口
    window.show()

    # 启动应用程序事件循环
    sys.exit(app.exec_())
