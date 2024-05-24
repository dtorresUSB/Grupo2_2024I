import serial
import time

def comunicar(dato):
    text=''
    ser=serial.Serial('COM4',baudrate=9600,timeout=1)
    primer='I'
    ser.write(primer.encode('utf-8'))
    time.sleep(1.9)
    ser.write(dato.encode('utf-8'))
    time.sleep(0.8)
    try:
        while ser.in_waiting>0:
            line=ser.readline(ser.in_waiting).decode('ascii')
            print(line)
            text+=line
    except:
        print('Error de lectura')
    return line
        


if __name__=="__main__":
    ang=input('Dato de envio: ')
    comunicar(ang)