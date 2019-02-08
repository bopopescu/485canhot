# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import serial
import time

_modbusarray = bytearray()
_modbusarray.append(58)
_modbusarray.append(54)
_modbusarray.append(49)
_modbusarray.append(48)
_modbusarray.append(50)
_modbusarray.append(48)
_modbusarray.append(48)
_modbusarray.append(48)
_modbusarray.append(48)
_modbusarray.append(48)
_modbusarray.append(48)
_modbusarray.append(48)
_modbusarray.append(49)
_modbusarray.append(57)
_modbusarray.append(67)
_modbusarray.append(13)
_modbusarray.append(10)

read=True
EN_485=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN_485,GPIO.OUT)
conn= serial.Serial("/dev/ttyAMA0",9600,timeout=0.5)
while read:
	#print("send Data")
    GPIO.setup(EN_485,GPIO.OUT)
    GPIO.output(EN_485,GPIO.HIGH)
    conn.write(_modbusarray)
    #DONT CHANGE IT
    time.sleep(0.02)
    GPIO.output(EN_485,GPIO.LOW)
    
    str=conn.readline()
    if str:
      print("get str:"+str)
    else:
		conn.close()
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		#DONT CHANGE IT
   		conn= serial.Serial("/dev/ttyAMA0",9600,timeout=0.5)

time.sleep(0.5)
