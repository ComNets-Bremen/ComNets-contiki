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

with open("rcvddata.csv", "a") as csvFile:
        csvwriter = csv.writer(csvFile, delimiter=";")
        logging.info("Opened CSV file")
        while True:
            data = []
            try:
                        
                    data = ser.readline()
                    data1 = time.strftime('%H:%M:%S ') + data
                    print(data)		    
	
                    csvwriter.writerow(data1.split())
                    logging.info("Written data in file")

            except KeyboardInterrupt as e:
                # Break out of loop only when user presses CTRL+C
                logging.error("Keyboard interrupt triggered")
                break
            except:
                logging.error("All other errors bypassing!")
                pass

        ser.close()

