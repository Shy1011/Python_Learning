import hid

# 枚举设备
for device in hid.enumerate():
    print(f"Device: {device['product_string']} Vendor ID: {device['vendor_id']} Product ID: {device['product_id']}")

# 尝试打开一个设备（这里需要替换为你的设备的vendor_id和product_id）
vendor_id = 0x046d  # 举例：Logitech的Vendor ID
product_id = 0xc534  # 举例：某个Logitech产品的Product ID
try:
    device = hid.device()
    device.open(vendor_id, product_id)  # 打开设备

    # 设置非阻塞模式
    device.set_nonblocking(1)

    # 发送数据（这里的数据和报告ID需要根据你的设备来定）
    device.write([0x0, 0xff, 0xff, 0xff])

    # 读取数据
    data = device.read(64)
    print(data)

finally:
    device.close()  # 关闭设备

