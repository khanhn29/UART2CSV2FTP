#!/usr/bin/python

import time
import serial

ser = serial.Serial(
        port = '/dev/ttyAMA1',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
)

print("Raspberry's receiving : ")

try:
    while True:
        s = ser.readline()
        print(s)
        data = s.decode()                       # decode s
        data = data.rstrip()                    # cut "\r\n" at last of string
        print(data)                             # print string

except KeyboardInterrupt:
        ser.close()
