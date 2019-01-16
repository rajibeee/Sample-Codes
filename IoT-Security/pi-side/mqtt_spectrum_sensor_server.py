## For controller#
import selectors2 as selectors
import socket

#################################SSL part ###################
import ssl
#######################################################
#######################
# GPA Mocule Imports  #
#######################
import gps
#######################

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
import os # Mosquitto sub pub running
import paho.mqtt.client as mqtt # mqtt running
import paho.mqtt.publish as publish # mqtt running

#np.set_printoptions(threshold=np.inf) # Needed to print all the array values
############################
# Setting up the GPS module #
#############################
session = gps.gps('localhost', '2947')
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
# Need to run the following commands in a terminal only once
# sudo systemctl stop gpsd.socket
# sudo systemctl disable gpsd.socket
# sudo systemctl stop serial-getty@ttyS0.service
# sudo systemctl disable serial-getty@ttyS0.service
# These commands need to be run after every reboot
# sudo killall gpsd
os.system("sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock") # Needed every reboot
#############################

sdr = RtlSdr()

# configure device--------------------
sdr.sample_rate = 2.048e6  # Hz
#sdr.center_freq = 70e6     # Hz
sdr.DEFAULT_READ_SIZE = 0.2e6 # Bandwidth in MHz
#sdr.bandwidth = 2e6 Trying new way to set bandwidth
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'
start=70e6 # Starting from 70MHz
end=80e6 #Ending at 80MHz
jump=1e6  #Incrementing by 1MHz from start to end
samplessent=0
numberofloops=0

# Hard-coded GPS value
lat= 28.6005417
lon=-81.1974785

start=int(start)
end=int(end)
jump=int(jump)
#-----------MQTT part--------------#
##client = mqtt.Client()
mqtt_port=8883
mqtt_dest_ip="192.168.0.101"
client= mqtt.Client("P1")
##----TLS for MQTT----##
#client.tls_set_context(context=None)

client.tls_set(ca_certs="/home/pi/Desktop/Project_CAP6133/SSL-Test/ca.crt", certfile="/home/pi/Desktop/Project_CAP6133/SSL-Test/client1.crt.pem", keyfile="/home/pi/Desktop/Project_CAP6133/SSL-Test/client1.key.pem", cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS, ciphers=None)
####------TLS part End-----##

client.connect(mqtt_dest_ip, mqtt_port)
client.subscribe("group4")
print "MQTT target IP:", mqtt_dest_ip
print "MQTT target port:", mqtt_port

####---Needed for controller---##
buf = ''
sep = ' '
freq_buf=''
bw_buf=''


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
#server.setpocket(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) ##Added on 24th Nov, to allow reuse
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

########### SSL Part for controller ########
#conn, addr = server.accept()
server = ssl.wrap_socket(server, server_side=True,certfile="/home/pi/Desktop/Project_CAP6133/SSL-Test/raspberrypi.crt",
                         keyfile="/home/pi/Desktop/Project_CAP6133/SSL-Test/raspberrypi.key", ssl_version=ssl.PROTOCOL_TLSv1)

#ssl.SSLSocket.cipher(TLSv1)

########### SSL for controller End ##########


mysel.register(server, selectors.EVENT_READ, accept)
start=int(start)
end=int(end)
jump=int(jump)

##-----------------------Controller part end-------------------#


while keep_running:
    print('waiting for I/O')
    import time
    time.sleep(10) #Set sleep time according to the frequency needed
    for sdr.center_freq in range(start, end, jump):
   		samplessent+=1 #Counting the number of samples being sent
		@limit_calls(1) #How many readings per frequency ?
		def process_send(samples, sdr):
			name=socket.gethostname()
			password="netmoc-lab"
			###-----Getting values from GPS-----#
			lat = gpsData['lat']
                        lon = gpsData['lon']
                        #-----End of GPS value----##
			import time
			ts = time.time()
			time=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d:%H:%M:%S')
			i=[np.square(samples.real)]
                        q=[np.square(samples.imag)]
			total = pack('4sffff19s10s', name, 10*log10(np.square(np.mean(i))+np.square(np.mean(q))), lat,lon, sdr.center_freq, time, password)
						
			#------------------MQTT Part-------------------#
			mqtt_topic = "group4"
			mqtt_msg= str(name)+"*"+ str(10*log10(np.square(np.mean(i))+np.square(np.mean(q))))+ "*"+ str(lat) + "*"+ str(lon) + "*"+ str(sdr.center_freq)+ "*" + str(time)
			print "mqtt_msg =", mqtt_msg
			client.publish(mqtt_topic, total)
			
                        #------------------End of MQTT Part-------------------#
			
		# ------------ Code for ctrl-c Exit----------##
		def signal_handler(signal, frame):
			print("\nprogram exiting gracefully")
			print "Samples sent outside =", samplessent*2 #Have to multiply by the number of times each frequency is accessed
			print "Number of loops =", numberofloops
                        #s.close();
			sys.exit(0)
		signal.signal(signal.SIGINT, signal_handler)

		# - - - - - - - - - - - Calling the sending function - - - - - - -#

		sdr.read_samples_async(process_send)
############################################################################################
    for key, mask in mysel.select(timeout=1):
      	callback = key.data
        callback(key.fileobj, mask)

print('shutting down')
mysel.close()


