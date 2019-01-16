#selectors_echo_server.py
import selectors2 as selectors
import socket

from rtlsdr import RtlSdr
from rtlsdr import *
from numpy import *
import numpy as np
import struct
from struct import *
import sys, signal ## Needed to exit the program using ctrl+c
import time ## Need to have time stamp
import datetime 
import socket
import xlwt # printing in xls
import xlsxwriter
# Mosquitto sub pub running
import paho.mqtt.client as mqtt # mqtt running
import paho.mqtt.publish as publish # mqtt running
np.set_printoptions(threshold=np.inf) # Needed to print all the array values

sdr = RtlSdr()

# configure device--------------------
sdr.sample_rate = 2.048e6  # Hz
#sdr.center_freq = 70e6     # Hz
sdr.DEFAULT_READ_SIZE = 0.2e6 # Bandwidth in MHz
#sdr.bandwidth = 2e6 Trying new way to set bandwidth
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'
start=70e6
end=75e6
jump=1e6
samplessent=0
numberofloops=0
lat= 28.6005417
lon=-81.1974785

start=int(start)
end=int(end)
jump=int(jump)

#######################################################
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

###################################################

mysel = selectors.DefaultSelector()
keep_running = True
sep=' '

def read(connection, mask):
    "Callback for read events"
    global keep_running

    client_address = connection.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # A readable client socket has data
        print('  received {!r}'.format(data))
	#   connection.sendall(data)
################################################################
	print "Received: ", data
        freq_buf= data[0:data.index(sep)]
        bw_buf= data[data.index(sep)+1:len(data)-1]
        print ("freq buf %s" % freq_buf)
        print ("bw buf %s" % bw_buf)
 	global start
	start=int(freq_buf)*1000000
        global end
	end=int(bw_buf)*1000000
       # start= (int(freq_buf) - int(int(bw_buf)/2))*1000000
       # end = (int(freq_buf) + int(int(bw_buf)/2))*1000000    
        print ("Start %d End %d and Jump %d" % (start, end, jump))
###################################################################
    else:
        # Interpret empty result as closed connection
        print('  closing')
        mysel.unregister(connection)
        connection.close()
        # Tell the main loop to stop
       # keep_running = False


def accept(sock, mask):
    "Callback for new connections"
    new_connection, addr = sock.accept()
    print('accept({})'.format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)


server_address = ("0.0.0.0", 1234)
print('starting up on {} port {}'.format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)
start=int(start)
end=int(end)
jump=int(jump)
flag =0

while keep_running:
	print('waiting for I/O')
	import time
	#time.sleep(3)
	if flag==1:
		start=80e6
		end=85e6
		start=int(start)
		end=int(end)
	if flag==20:
		start=60e6
		end=65e6
		start=int(start)
		end=int(end)
	flag=flag+1
	for sdr.center_freq in range(start, end, jump):
		samplessent+=1
		@limit_calls(1)
		def process_send(samples, sdr):
			name=socket.gethostname()
			password="netmoc-lab"
			import time
			ts = time.time()
			time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d:%H:%M:%S')
			i=[np.square(samples.real)]
			q=[np.square(samples.imag)]
			total = pack('4sffff19s10s', name, 10*log10(np.square(np.mean(i))+np.square(np.mean(q))), lat,lon, 				sdr.center_freq, time, password)
			print "It's working..."
			
			
			global book_index
			global sheet1
			book_index = book_index+1
			sheet1.write(book_index, 0, "pi-4" )
			sheet1.write(book_index, 1, 10*log10(np.square(np.mean(i))+np.square(np.mean(q))))
			sheet1.write(book_index, 2, lat)
			sheet1.write(book_index, 3, lon)
			sheet1.write(book_index, 4, sdr.center_freq)
			sheet1.write(book_index, 5, time)
			
			
			
			#------------------MQTT Part-------------------#
			
			
                        #------------------End of MQTT Part-------------------#
			
		# ------------ Code for ctrl-c Exit----------##
		def signal_handler(signal, frame):
			print("\nprogram exiting gracefully")
			print "Samples sent outside =", samplessent*2 #Have to multiply by the number of times each frequency is accessed
			print "Number of loops =", numberofloops
                        #s.close();
			global book_index
                        global chart 
                        global sheet1
                        chart.add_series({
                                	'name':       '=Sheet1!$B$1',
                                	'categories': '=Sheet1!$E$2:$E$120',
                                	'values':     '=Sheet1!$B$2:$B$120',
                        })
	# Set an Excel chart style. Colors with white outline and shadow.
                        chart.set_style(10)

	# Insert the chart into the worksheet (with an offset).
                        sheet1.insert_chart('G2', chart, {'x_offset': 25, 'y_offset': 10})
			sys.exit(0)
		signal.signal(signal.SIGINT, signal_handler)

		# - - - - - - - - - - - Calling the sending function - - - - - - -#

		sdr.read_samples_async(process_send)
############################################################################################
	time.sleep(3600)
	for key, mask in mysel.select(timeout=1):
      		callback = key.data
    	  	callback(key.fileobj, mask)

print('shutting down')
mysel.close()

