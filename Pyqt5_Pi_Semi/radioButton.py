import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RadioDemo(QWidget):
    def __init__(self,parent=None):
        super(RadioDemo,self).__init__(parent)
        #水平布局
        layout=QHBoxLayout()


        self.btn1=QRadioButton('Button1')
        #默认选中btn1
        self.btn1.setChecked(True)
        #toggled信号与槽函数绑定
        self.btn1.toggled.connect(lambda :self.btnstate(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2 = QRadioButton('Button2')
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))
        layout.addWidget(self.btn2)

        self.setLayout(layout)
        self.setWindowTitle('RadioButton demo')

    def btnstate(self,btn):
    #输出按钮1与按钮2的状态，选中还是没选中
        if btn.text()=='Button1':
            if btn.isChecked()==True:
                print(btn.text()+"is selected")
            else:
                print(btn.text()+"is deselected")

        if btn.text()=="Button2":
            if btn.isChecked() == True:
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deselected")
if __name__ == '__main__':
    app=QApplication(sys.argv)
    radioDemo=RadioDemo()
    radioDemo.show()
    sys.exit(app.exec_())