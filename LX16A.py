


import serial
import struct


class LX16A:
    """ 
    Class for driving LewanSoul LX-16A Servos 
    """


    def __init__ (self):
    	self.port = None

    def connect (self):
    	p = serial.Serial()
    	p.baudrate = 115200
    	p.port = '/dev/ttyUSB0'
    	p.timeout = 0.5
    	p.open()

    	if p.is_open:
    	    self.port = p

     def close(self):
     	if self.port.is_open:
     	    self.port.close()
     	    self.port = None

     def send(self, servo_id, command_id, data=None)
     


