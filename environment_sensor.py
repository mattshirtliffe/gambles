import serial
import time
from client import Gambles

# todo clean and refactor this

client = Gambles()
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()
if ser.is_open:
    while True:
        line = ser.readline().decode()
        if ':' in line:
            bucket_type, value = line.split(':')
            # clean value
            value = value.strip()
            key = str(time.time())
            print(key)
            response = client.store('sensor', {"value":value,"type":bucket_type},key=key)
            print(response)
else:
    print('Error opening serial')