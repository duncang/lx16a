#!/bin/python

import serial
import time
import struct 

print "PySerial Version: " + serial.VERSION

print("Openining /dev/ttyUSB0")

p = serial.Serial()
p.baudrate = 115200
p.port = '/dev/ttyUSB0'
p.timeout = 0.5
p.open()

print ("Opened " + p.name)



# construct a message
# 0xFE = broadcast ID 
servo_id=2
packet = [0x55, 0x55]
packet.append(servo_id)
length=3

 

# commands
# SERVO_MOVE_TIME_WRITE = 1
# SERVO_ID_READ = 14
cmd = 1
#data = None

data = [0x00, 0x00, 0x00, 0x00]

length = length + 4


position = 0300
time = 1000

data = bytearray(struct.pack('hh',position,time))

packet.append(length)
packet.append(cmd)

checksum = servo_id + length + cmd
#if data is not None:
for d in data:
    packet.append(d)
    checksum = checksum + d

checksum = (~checksum) & 0xFF

packet.append(checksum)

bytes_to_send = bytearray(packet)

print("Sending: " + str(packet))

p.write(bytes_to_send)

response = bytearray(p.read(7))

print("Received: ")
print ''.join('{:d} '.format(x) for x in response)


