import time
import serial
from threading import Thread

num = 0

HAPPY = '1'
DANGER = '2'
DANCE = '3'
LOVE = '4'
SPEAK = '5'

while True:
    try:
        print("Trying serial ACM" + str(num))
        ser = serial.Serial(
            port='/dev/ttyACM'+ str(num),
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)
    except:
        if num < 10:
            num += 1
        else:
            break

def send_to_arduino(message):
    try:
        Thread(target=ser.write, args=[message,]).start()
    except:
        pass
