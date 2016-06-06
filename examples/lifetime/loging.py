#!/usr/bin/env python
import serial
import csv
import time

while (1):
        data = [];
        ser = serial.Serial(
        port='/dev/ttyUSB1',
        baudrate=115200,
        )
        csvfile= open("batterystatus.csv", "a")
        csvwriter = csv.writer(csvfile, delimiter=";")
        while True:
                try:
                        data= ser.readline()
                        print(data)
                        data1=time.strftime('%H:%M:%S ') + data
                        csvwriter.writerow(data1.split())
                except KeyboardInterrupt:
                        print('Timeout: Did not received any data')
        ser.close()
        csvfile.close()

