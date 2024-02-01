'''

动态显示当前时间

QTimer
QThread

多线程：用于同时完成多个任务




'''

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import sys


class ShowTime(QWidget):

    def __init__(self, parent=None):
        super(ShowTime, self).__init__(parent)
        self.setWindowTitle("动态显示当前时间")

        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        layout= QGridLayout()

        self.timer = QTimer()  # 创建了一个计时器对象
        self.timer.timeout.connect(self.showTime) # 将计时器对象的 超时连接到 一个槽函数上 一旦计时器超时则调用这个函数

        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()

        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000) # 1000ms的超时
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()   # 停止计时器
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec_())