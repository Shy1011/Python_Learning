#!/usr/bin/python3
import time
import hid

perepherialBrg = { } # 创建一个空字典


"""
列出所有的USB设备的信息并打印出来
"""
def listAllDev() :
    for device_dict in hid.enumerate(): # 遍历hid这个字典列表
        keys = list(device_dict.keys()) # 一个字典的键值的列表
        print(keys)
        for key in keys:
            print("%s : %s" % (key, device_dict[key]))
        print()

# listAllDev()

"""
找到 manufacturer_string为wch.cn的设备
"""
def findBrg(name) :
    device = hid.enumerate()
    for perepherial in device:
        keys = list(perepherial.keys())
        for key in keys:
            if perepherial["manufacturer_string"] == name : # "wch.cn"
                # print("%s : %s" % (key,perepherial[key],))
                return perepherial



"""
打印USB设备的信息
"""
def printBrgInfo(perepherialBrg) :
    keys = list(perepherialBrg.keys())
    for key in keys:
        print("%s : %s" % (key,perepherialBrg[key],))


perepherialBrg = findBrg("wch.cn")
printBrgInfo(perepherialBrg)

#_________________________________________________________________________________

try:
    print("Opening the device")

    h = hid.device()
    h.open(6790, 65031)  # TREZOR VendorID/ProductID

    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    print("Write the data")
    h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    time.sleep(0.05)

    # read back the answer
    print("Read the data")
    while True:
        d = h.read(64)
        if d:
            print(d)
        else:
            break

    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")