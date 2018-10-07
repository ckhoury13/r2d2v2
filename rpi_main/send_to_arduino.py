import time
import serial


ser = serial.Serial(
  
   port='/dev/ttyUSB0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1)

HAPPY = '1'
DANGER = '2'
DANCE = '3'
LOVE = '4'
SPEAK = '5'

def sendToArduino(message):
   ser.write(message)
   print('Sending ' + message)

