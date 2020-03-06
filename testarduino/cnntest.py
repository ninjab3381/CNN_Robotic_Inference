import serial
recyclable_lbl = ['alfoil', 'box', 'cbcontainer', 'cokecan', 'milkcan', 'plasticbottle', 'spoon']
predicted_cls = 'alfoil'
with serial.Serial('/dev/ttyUSB0',9600,timeout=100) as ser:
    if predicted_cls in recyclable_lbl:
        #print("It is Recyclable")
        ser.write(bytes('Y\n','utf-8'))
    else:
        #print("It is Not Recyclable")
        ser.write(bytes('N\n','utf-8'))
