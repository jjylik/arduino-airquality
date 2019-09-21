import serial
import subprocess
from time import sleep, time
import datetime

ser = serial.Serial("COM3", 9600, timeout=5)
now = datetime.datetime.now()
outputfile = "output_"+now.strftime("%d-%m-%y")+".csv"
output = open(outputfile,"w", 1)
sleep(0.2)
print("Starting air quality measurements, logging to "+outputfile)

try:
	while True:
		received = ser.readline().decode().strip()
		if received:
			output.write(received+","+datetime.datetime.now().strftime("%X")+"\n")
except KeyboardInterrupt:
	pass
ser.close()
output.close()