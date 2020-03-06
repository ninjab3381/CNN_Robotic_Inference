import serial
with serial.Serial('/dev/ttyUSB0',9600,timeout=100) as ser:
    while True:
        led_on = input('Do you want the LED on? ')[0]
        if led_on in 'yY':
            ser.write(bytes('Y\n','utf-8'))
        if led_on in 'Nn':
            ser.write(bytes('N\n','utf-8'))
