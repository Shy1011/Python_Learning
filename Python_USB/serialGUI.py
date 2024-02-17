from PyQt5.QtWidgets import *
import sys
from SerialPort import  Ui_Form
from Serial_01 import SerialPort

class SerialGUI(QWidget,Ui_Form):
    state = True
    def __init__(self):
        super().__init__()
        self.ser = SerialPort() # 创建端口实例
        self.ser.defaultSet()

        self.setupUi(self) # UI 初始化设置
        self.portSearch() # 搜索 串口端口

        self.comboBox.currentIndexChanged.connect(self.updateLabel_1)  # combo_2 槽函数
        self.comboBox_2.currentIndexChanged.connect(self.updateLabel_2) # combo_2 槽函数
        self.radioButton.toggled.connect(self.changeSerialState)
        self.pushButton.clicked.connect(self.sendMessage)

    def sendMessage(self):
        self.ser.sendData(self.lineEdit_2.text())

    def changeSerialState(self):
        self.state = not self.state
        if self.state :
            self.ser.closeSerial()
            print("Serial Close")
        else :
            self.ser.openSerial()
            print("Serial Open")


    def updateLabel_1(self): # 波特率的自定义设置
        self.ser.setPort(self.comboBox.currentText()) # 一旦combo
        print(f"Port is {self.comboBox.currentText()}")
    def updateLabel_2(self): # 波特率的自定义设置
        if self.comboBox_2.currentText() == "Custom" :
            self.comboBox_2.setEditable(True)
        else :
            self.comboBox_2.setEditable(False)
        self.ser.setBaudrate(self.comboBox_2.currentText()) # 一旦combo
        print(f"Baudrate is {self.comboBox_2.currentText()}")


    def portSearch(self): # Port号的搜索

        self.ports = self.ser.searchPort()
        self.ports.sort()
        for port in self.ports :
            self.comboBox.addItem(f"{port}")




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = SerialGUI()
    win.show()
    sys.exit(app.exec_())  # 运行应用程序，直到退出