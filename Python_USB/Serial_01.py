import serial

ser = serial.Serial("COM2", 9600, timeout=0.01)

while True:
    data = ser.read_all()
    if data:
        rec_str = data.decode('utf-8')
        print(rec_str)

