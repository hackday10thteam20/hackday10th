import sys
import serial
import os
import time
import random

class Ballon:
    usb = '/dev/tty.usbmodem1411' 
    port = 9600
    message = "b\r"
    ser = serial.Serial(usb, port, timeout=10)

    def send(self, on):
        if on == True:
            self.message = "a\r"
            #print(self.message)
        else:
            self.message = "b\r" 
        self.ser.write(self.message.encode())
            #print(self.message)

    def  __del__(self):
        self.ser.close()
