# -*- coding:utf-8 -*-
import serial
import time

#t = serial.Serial("/dev/ttyAMA0",9600)    
t = serial.Serial("/dev/ttyS0",9600,timeout=1)
print t.portstr    

strInput = ':210F000000040102C9\r\n'
n = t.write(strInput)    
print strInput

while 1:  
    str = t.readall()  
    if str:  
        print str 
