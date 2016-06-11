#!/usr/bin/env python3

# Python 3 is better in terms of fileIO

from serial import Serial
import csv
import time
import logging

# Logging Setup

logging.basicConfig(filename = 'lifetime.log', level=logging.INFO)

# change also check for timeout in the Serial () function 

while (1):
        data = [];
	# get data from serial port
        ser = Serial(
	# Change the port for usb
        port='/dev/ttyUSB1',
	# Change the baud rate
        baudrate=115200,
        )

        logging.info("Serial Port opened")

        with open("batterystatus.csv", "a") as csvwriter:
            csvwriter = csv.writer(csvfile, delimiter=';')
            logging.info("CSV file opened")

            while True:
                    try:
                            data= ser.readline()
                            if not data:
                                break
                            print(data)
                            data1=time.strftime('%H:%M:%S ') + data
                            csvwriter.writerow(data1.split())
                            logging.info("Data written in file")

                    except KeyboardInterrupt as e:
                        raise e
                        logging.error("Keyboard Interrupt/Timeout Triggered")
                        print('Timeout: Did not receive data')
                        pass
            ser.close()

