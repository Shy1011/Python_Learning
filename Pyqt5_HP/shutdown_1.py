import sys
from PyQt5.QtWidgets import *
from shutdown import *
import os
import time
import threading

class Win(QWidget,Ui_Form):
    time1 = 100 # /mins
    count = 0;
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setUI()
    def initUI(self):
        self.setupUi(self)


    def setUI(self):
        # 连接槽函数到按钮的 clicked 信号
        self.sliderTime.valueChanged.connect(self.theValueOfTheSliderShow)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.lineEdit.textChanged.connect(self.textChanged)

    def theValueOfTheSliderShow(self):
        print(self.sender().value())
        self.time.setText(str(self.sender().value()))

    def accept(self):
        print("Accept")
        time1 = int(self.lineEdit.text()) # 字符串转为整形
        self.time1 = time1
        print(time1)
        # time.sleep(time1)
        # 执行电脑休眠命令
        print("休眠")
        # os.system("shutdown /h")


    def reject(self):
        print("Reject")
        self.count = self.time1
        self.timer = threading.Timer(1, self.my_function)
        if self.count > 0 :
            self.count = self.count - 1
            self.timer.start()
            print(self.count)

    def my_function(self):
        print("Time Out")

        # if self.count == self.time :
        #     self.label_3.setText()
        # print(self.count)

    def textChanged(self):
        time = self.sender().text()
        print(time)

    def sleep_after_minutes(self,secs):
        # 将分钟转换为秒
        # seconds = minutes * 60
        # 等待指定的时间
        time.sleep(secs)
        # 执行电脑休眠命令
        os.system("shutdown /h")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())