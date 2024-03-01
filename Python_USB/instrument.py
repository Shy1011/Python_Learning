"""
读取万用表电压的值/电流的值
"""
import pyvisa

# 创建资源管理器实例
rm = pyvisa.ResourceManager()

# 打开与万用表的会话，替换为你的万用表VISA地址
multimeter = rm.open_resource('USB0::0x2184::0x0059::GEW912502::INSTR')

# 配置万用表为电压测量模式，具体命令根据万用表型号和手册确定
multimeter.write('CONF:VOLT:DC AUTO') # 设置为DC电压测量模式 量程自选
# multimeter.write('CONF:CURR:DC AUTO') # 设置为DC电流测量模式 量程自选
# 会将万用表配置为远程模式,要想实时测量需要按下shift(local)按键

# 读取电压值
voltage = multimeter.query('READ?')

# 监测电压直到值小于
while(True) :
    voltage = multimeter.query('READ?')
    value = abs(2.50 - float(voltage))
    if(value < 0.02) :
        print("Pass")
        break


print(f"Measured Voltage: {voltage} V")
print(type(voltage))
print(float(voltage))
# 关闭会话
multimeter.close()