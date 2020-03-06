import serial

with serial.Serial('/dev/ttyUSB0',9600,timeout=100) as ser:
    while True:
        print(ser.readline())
