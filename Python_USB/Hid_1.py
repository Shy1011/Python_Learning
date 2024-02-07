import hid

for device_dict in hid.enumerate(): # list [dics]
    keys = list(device_dict.keys()) # 取出 dics中的键值
    keys.sort() # 按照键值排序
    for key in keys: #
        print("%s : %s" % (key, device_dict[key]))
    print()