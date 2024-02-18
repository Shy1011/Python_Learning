from PyQt5.QtWidgets import *
import sys
from SerialPort import  Ui_Form
from Serial_01 import SerialPort
from hintDialog import portHasBeenOpened
import threading
from PyQt5.QtCore import pyqtSignal
import time
from thread import  CountThread
class SerialGUI(QWidget,Ui_Form):
    text = "Hello"
    state = True
    threadFlag = True
    # 定义一个信号，用于接收串口数据
    receive_data_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ser = SerialPort() # 创建端口实例
        self.ser.defaultSet()

        self.setupUi(self) # UI 初始化设置
        self.portSearch() # 搜索 串口端口
        self.textBrowser.setText("")

        self.comboBox.currentIndexChanged.connect(self.updateLabel_1)  # combo_2 槽函数
        self.comboBox_2.currentIndexChanged.connect(self.updateLabel_2) # combo_2 槽函数
        self.radioButton.toggled.connect(self.changeSerialState)
        self.sendData.clicked.connect(self.sendMessage)
        self.receive_data_signal.connect(self.update_received_data)


    def sendMessage(self):
        self.ser.sendData(self.textEdit.toPlainText())

    def changeSerialState(self):   # 开关串口的端口
        self.state = not self.state
        if self.state :
            try :
                self.threadFlag = False
                self.ser.closeSerial()
                print("Serial Close")

            except :
                print("Something is Wrong")

        else :
            try :
                self.threadFlag = True
                self.ser.openSerial()
                time_thread = threading.Thread(target=self.recData)
                time_thread.start()
                print("Serial Open")



            except :
                print("The port has already been opened")
                win = portHasBeenOpened()
                win.exec()



    def updateLabel_1(self): # 端口选择
        self.ser.setPort(self.comboBox.currentText()) # 列表的文本选择
        print(f"Port is {self.comboBox.currentText()}")

    def updateLabel_2(self): # 波特率的自定义设置
        if self.comboBox_2.currentText() == "Custom" :
            self.comboBox_2.setEditable(True)
        else :
            self.comboBox_2.setEditable(False)
        self.ser.setBaudrate(self.comboBox_2.currentText()) # 列表的文本选择
        print(f"Baudrate is {self.comboBox_2.currentText()}")


    def portSearch(self): # Port号的搜索

        self.ports = self.ser.searchPort()
        self.ports.sort()
        for port in self.ports :
            self.comboBox.addItem(f"{port}")

    def recData(self):
        while(self.threadFlag):
            data = self.ser.ReceiveData()
            # 发送串口数据信号到主线程
            self.receive_data_signal.emit(data)

    def update_received_data(self,data): # receive_data_signal的槽函数
        self.textBrowser.append(data)

    def closeEvent(self, event):
        # 在关闭窗口时执行的操作
        print("Widget is being closed")
        # 如果你想要完全退出应用程序，可以调用QApplication的quit()方法
        # QApplication.instance().quit()
        self.threadFlag = False # 关闭进程
        event.accept()  # 接受关闭事件

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = SerialGUI()
    win.show()
    sys.exit(app.exec_())  # 运行应用程序，直到退出
