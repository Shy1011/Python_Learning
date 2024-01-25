import hid

pBdg = hid.device()       # create hid device
pBdg.open(0x1A86, 0xFE07)
