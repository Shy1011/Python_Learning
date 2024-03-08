import pyvisa
"""
在字符串USB0::0x2184::0x0059::GEW912502::INSTR中，每个部分的含义如下：   

- USB0：表示通信接口类型，这里是USB。

- 0x2184：表示设备的Vendor ID（制造商识别码），以十六进制表示。

- 0x0059：表示设备的Product ID（产品识别码），以十六进制表示。

- GEW912502：表示设备的序列号或者其他标识符。

- INSTR：表示设备的类型，这里是仪器（Instrument）。

这个字符串是一个VISA资源地址的示例，用于标识连接到计算机的仪器。
在这种格式中，各个部分通过双冒号::分隔，通常用于在PyVISA等库中指定要连接的仪器。 
"""

# 创建资源管理器
rm = pyvisa.ResourceManager()
#
# # 打印可用的资源（仪器）列表
print(rm.list_resources()) # 打印出所有万用表的地址
#
# # 打开与仪器的会话（这里需要替换为你的仪器地址）
# my_instrument = rm.open_resource('USB0::0x2184::0x0059::GEW912502::INSTR')
# #
# # # 查询仪器标识
# print(my_instrument.query('*IDN?'))
# #
# # # 关闭会话
# my_instrument.close()
