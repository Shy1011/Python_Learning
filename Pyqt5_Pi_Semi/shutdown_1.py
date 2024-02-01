import sys
from PyQt5.QtWidgets import *
from shutdown import *

class Win(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setUI()
    def initUI(self):
        self.setupUi(self)


    def setUI(self):
        self.sliderTime.valueChanged.connect(self.theValueOfTheSliderShow)
        print(self.sliderTime.value())

        # 连接槽函数到按钮的 clicked 信号
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def theValueOfTheSliderShow(self):
        print(self.sender().value())
        self.time.setText(str(self.sender().value()))

    def accept(self):
        print("Accept")

    def reject(self):
        print("Reject")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())