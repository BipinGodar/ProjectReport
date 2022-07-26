import serial
import time
arduinodata=serial.Serial('com4',9600)

def led_on():
    arduinodata.write('1')

def led_off():
    arduinodata.write('0')

time.sleep(5)
print("done")