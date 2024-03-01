from PyQt5.QtWidgets import *
import sys
from SerialPort import  Ui_Form
from Serial_01 import SerialPort
from hintDialog import portHasBeenOpened
import threading
from PyQt5.QtCore import pyqtSignal
from datetime import datetime
import time
from thread import  CountThread
class SerialGUI(QWidget,Ui_Form):
    text = "Hello"
    state = False
    threadFlag = True
    dataNumber = 0
    dataSent = 0
    ascllState = False
    timeShow = False
    autoSend = False
    # 定义一个信号，用于接收串口数据 可以触发槽函数的 详见 Readme.md
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
        self.checkBox_2.toggled.connect(self.AscllState) # ASCII HEX切换
        self.checkBox_2.setChecked(True)
        self.checkBox_8.toggled.connect(self.autoSent)
        self.checkBox_8.setChecked(False)
        self.checkBox.clicked.connect(self.changeSerialState)
        self.checkBox_5.toggled.connect(self.timeShowState)
        self.sendData.clicked.connect(self.sendMessage)
        self.ClearData.clicked.connect(self.clearData)
        self.receive_data_signal.connect(self.update_received_data)
        self.radioButton.toggled.connect(self.radioFunc1)
        self.radioButton.setChecked(True)
        self.radioButton_2.toggled.connect(self.radioFunc2)
        # self.radioButton_2.setChecked(True)


    def radioFunc1(self):
        if self.radioButton.isChecked() == True :
            print("1 is Checked")

    def radioFunc2(self):
        if self.radioButton_2.isChecked() == True :
            print("2 is Checked")

    def autoSent(self):
        self.autoSend = not self.autoSend
        print(self.autoSend)
        thread1 = threading.Thread(target=self.autoSend1)
        thread1.start()


    def autoSend1(self):
        try :
            while(self.autoSend and self.state) :
                time.sleep(float(self.lineEdit.text()))
                print("Autosend Message")
                self.ser.sendData(self.textEdit.toPlainText())
                self.dataSent = self.dataSent + len(self.textEdit.toPlainText())
                self.label_9.setText(f'Rx : {str(self.dataSent)}')
        except :
            print("The port has already been opened")
            # win = portHasBeenOpened()
            # win.exec()

    def AscllState(self):
        self.ascllState = not self.ascllState
        print(self.ascllState)
        if self.ascllState == True :
            self.label_11.setText("ASCII")
        else :
            self.label_11.setText("HEX")

    def timeShowState(self):
        self.timeShow = not self.timeShow
        print(self.timeShow)

    def sendMessage(self):
        try :
            self.ser.sendData(self.textEdit.toPlainText())
            self.dataSent = self.dataSent + len(self.textEdit.toPlainText())
            self.label_9.setText(f'Rx : {str(self.dataSent)}')
        except :
            print("The port has already been opened")
            win = portHasBeenOpened()
            win.exec()

    def changeSerialState(self):   # 开关串口的端口
        self.state = not self.state
        if self.state == False :
            try :
                self.threadFlag = False
                self.ser.closeSerial()
                print("Serial Close")
                self.label_10.setText("Close")

            except :
                print("Something is Wrong")

        else :
            try :
                self.threadFlag = True
                self.ser.openSerial()
                time_thread = threading.Thread(target=self.recData)
                time_thread.start()
                print("Serial Open")
                self.label_10.setText("Open")



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
            self.dataNumber = self.dataNumber + len(data[0]) # 获取接收到多少个字符串
            if self.ascllState == True :
                self.receive_data_signal.emit(data[0])
            else :
                self.receive_data_signal.emit(data[1])


    def update_received_data(self,data): # receive_data_signal的槽函数
        if self.timeShow == False :
            self.textBrowser.append(data)
        else :
            current_time = datetime.now()

            # 格式化时间，只包括小时、分钟和秒
            formatted_time = current_time.strftime("%H:%M:%S")
            self.textBrowser.append(f'{formatted_time} {data}')

        self.label_8.setText(f'Rx : {str(self.dataNumber)}')
        # print("Current time:", datetime.now())

    def clearData(self):
        self.textBrowser.setText("")
        self.dataNumber = 0
        self.dataSent = 0
        self.label_8.setText(f'Rx : {str(self.dataNumber)}')
        self.label_9.setText(f'Tx : {str(self.dataSent)}')

    def closeEvent(self, event):
        # 在关闭窗口时执行的操作
        print("Widget is being closed")
        # 如果你想要完全退出应用程序，可以调用QApplication的quit()方法
        # QApplication.instance().quit()
        self.threadFlag = False # 关闭进程
        self.autoSend = False  # 关闭进程
        event.accept()  # 接受关闭事件

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    win = SerialGUI()
    win.show()
    sys.exit(app.exec_())  # 运行应用程序，直到退出
