import serial
import os

class Balloon:
    usb = '/dev/tty.usbmodem14611' 
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
