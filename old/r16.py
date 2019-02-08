import os
import RPi.GPIO as GPIO
import time,serial
import modbusPoll as modbus

read=True
EN_485=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485, GPIO.OUT)
conn= serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
while read:
    for i in range(61, 76):
       try:
         GPIO.setup(EN_485, GPIO.OUT)
         GPIO.output(EN_485, GPIO.HIGH)
         conn.write(modbus.read_AI(i))
         time.sleep(0.02)
         GPIO.output(EN_485, GPIO.LOW)
         str=conn.readline()
         if str.decode("utf-8").find(":") >= 1:

           print((str.decode("utf-8")).split(":", 1)[1].strip())
         else:
           conn.close()
           GPIO.cleanup()
           GPIO.setmode(GPIO.BCM)
           #DONT CHANGE IT
           conn= serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
       except Exception as e:
            print(str(e))

       time.sleep(0.5)
