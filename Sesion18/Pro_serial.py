import serial

ser=serial.Serial('COM5',baudrate=9600)
while 1:
    dato=input('Que dato desea enviar: ')
    ser.write(dato.encode('utf-8'))
    try:
        line=ser.readline().decode('ascii')
        print(line)
    except:
        print('error')
