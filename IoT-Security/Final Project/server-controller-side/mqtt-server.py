from struct import *
import struct
import sys, signal ## Needed to exit the program using ctrl+c
import paho.mqtt.client as mqtt  #mqtt
#import paho.mqtt.subscribe as subscribe
#import paho.mqtt.client as mqtt #import the client1
import numpy as np
import math
import time
import xlwt # printing in xls
import xlsxwriter
#from OpenSSL import SSL
import ssl
import socket
###---------------------Excel Part------------------------#
book = xlsxwriter.Workbook('spectrum-data-1.xls')
sheet1 = book.add_worksheet()

sheet1.write(0, 0, "User")
sheet1.write(0, 1, "RSSI")
sheet1.write(0,2, "Lattitude")
sheet1.write(0,3, "Longitude")
sheet1.write(0,4, "Center Freq.")
sheet1.write(0,5, "Date-time")
book_index=0

# Charts are independent of worksheets
chart = book.add_chart({'type': 'line'})
chart.set_y_axis({'name': 'RSSI (dB)'})
chart.set_x_axis({'name': 'Center Frequency (MHz)'})
chart.set_title({'name': 'Frequency versus RSSI Plot'})
######------------------Excel Part End--------------------####

broker_address="192.168.0.102"  #Enter own IP
port=1883

def on_message(client,userdata,message):
	time.sleep(1)
	#print ("Received=", str(message.payload.decode("utf-8")))
	specific=unpack('4sffff19s10s', message.payload)
	print "User = ", specific[0], "db=", specific[1], "lat=", specific[2], ", lon=", specific[3], "Freq=",specific[4], "Time =", specific[5]

#######------------------ Excel Part-------------#####
	global book_index
	global sheet1	
	book_index = book_index+1
    	sheet1.write(book_index, 0, specific[0])
	sheet1.write(book_index, 1, specific[1])
	sheet1.write(book_index, 2, specific[2])
	sheet1.write(book_index, 3, specific[3])
	sheet1.write(book_index, 4, (int(specific[4])/1000000))
	sheet1.write(book_index, 5, specific[5])
	
print("creating new instance")
client = mqtt.Client("P3") #create new instance
####################TLS Connection for MQTT #############################

client.tls_set(ca_certs="/home/rajib/Project_CAP6133/ca.crt", certfile="/home/rajib/Project_CAP6133/client.crt.pem", keyfile="/home/rajib/Project_CAP6133/client.key.pem", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)

#################### End of TLS Connection for MQTT #############################
client.on_message=on_message
print("connecting to broker")
client.connect(broker_address,port) #connect to broker
print("Subscribing to topic","group4")
client.loop_start()
client.subscribe("group4")
time.sleep(86400) # Waiting for 24 hrs of data collection
client.disconnect()
client.loop_stop()
############################################
# Configure the first series.

chart.add_series({
    	'name':       '=Sheet1!$B$1',
    	'categories': '=Sheet1!$E$2:$E$50', # Increase the numbers for more data
    	'values':     '=Sheet1!$B$2:$B$50',
})
# Set an Excel chart style. Colors with white outline and shadow.
chart.set_style(10)

# Insert the chart into the worksheet (with an offset).
sheet1.insert_chart('G2', chart, {'x_offset': 25, 'y_offset': 10})

#############################################

def signal_handler(signal, frame): ## Stops the server by running ctrl+c
	#global book
	#book.save("spectrum-data-1.xls")
	print("\nprogram exiting gracefully")
	print "total number of sample received=", recvcounter
	############################################
	# Configure the first series.
	global book_index
	global chart 
	global sheet1
	chart.add_series({
    		'name':       '=Sheet1!$B$1',
    		'categories': '=Sheet1!$E$2:$E$5',
    		'values':     '=Sheet1!$B$2:$B$5',
	})
	# Set an Excel chart style. Colors with white outline and shadow.
	chart.set_style(10)

	# Insert the chart into the worksheet (with an offset).
	sheet1.insert_chart('G2', chart, {'x_offset': 35, 'y_offset': 10})

	#############################################
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


