#!/usr/bin/env python

import serial
import csv
import time
import logging

logging.basicConfig(filename = 'lifetime.log', level=logging.ERROR)




# get data from serial port
ser = serial.Serial(port='/dev/ttyUSB1',\
        baudrate=115200,\
        timeout = None)


# open file

with open("batterystatus.csv", "a") as csvFile:
        csvwriter = csv.writer(csvFile, delimiter=";")
        logging.info("Opened CSV file")
        while True:
                try:
                        data = [];
                        data = ser.readline()
                        # if no data break out of the loop
                        if not data:
                            break
                            logging.error("NO DATA")

                        data1 = time.strftime('%H:%M:%S ') + data

                        csvwriter.writerow(data1.split())
                        logging.info("Written data in file")

                except KeyboardInterrupt, e:
                    logging.error("This error occured",str(e))
                    break
                    ser.close()

