import serial # 安装pyserial 而不是 serial
from serial.tools import list_ports  # 找串口设备需要的包
"""
如果先安装了srerial 则需要删除serial这个库,执行一下代码.再去安装pyserial这是为了告诉编译器serial已经被删除了
否则编译器会找到错误的路径去
"""

class SerialPort():

    def openSerial(self):
        # ser = serial.Serial("COM2", 9600, timeout=0.01) # 这句话就是自动打开串口
        self.ser = serial.Serial()
        self.ser.port = "COM2"  # 不区分大小写
        self.ser.baudrate = 9600
        self.ser.timeout = 0.01
        self.ser.open()  # 打开端口

    def sendData(self):
        # 串口发送
        self.ser.write('Hello'.encode('utf-8')) # 发送数据


    def ReceiveData(self):
        # 串口接收
        while True:
            data = self.ser.read_all()

            if data:
                # print(data) #
                rec_str = data.decode('utf-8')
                print(rec_str)

    def searchPort(self):

        # 获取端口列表，列表中为 ListPortInfo 对象
        port_list = list(list_ports.comports())

        num = len(port_list)

        if num <= 0:
            print("找不到任何串口设备")
        else:
            for i in range(num):
                # 将 ListPortInfo 对象转化为 list
                port = list(port_list[i])
                # print(port)
                print(port[0]) # COM0 端口名字只是其中的一项

# ser.close() # 关闭端口

serial1 = SerialPort()
serial1.searchPort()