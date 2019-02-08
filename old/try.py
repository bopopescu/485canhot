# -*- coding:utf-8 -*-
import serial
import time

#t = serial.Serial("/dev/ttyAMA0",9600)
#t = serial.Serial("/dev/ttyS0",9600,timeout=1)
#t = serial.Serial("COM4",9600,timeout=1)
t = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=1)

strInput = ":210F000000040102C9\r\n".encode()
n = t.write(strInput)
#print (strInput)

str = t.readall()
if str:
    print (str)


'''
while 1:
    str = t.readall()
    if str:
        print (str)
'''
