import serial
import time
import datetime

def serial_data():
    data = serial.Serial(port="COM5", baudrate=9600, timeout=1, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)
    time.sleep(2)
    now = datetime.datetime.now()
    readOneByte = data.readline()
    #print(readOneByte.decode())
    if readOneByte:
        string = readOneByte.decode()
        with open("output.txt", "a") as file:
            file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {string}")
        