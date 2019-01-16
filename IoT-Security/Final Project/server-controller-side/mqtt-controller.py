import selectors2 as selectors
import socket
import ssl
mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
    b'It will be repeated.',
    b'This is the message.  ',
]
bytes_sent = 0
bytes_received = 0

# Connecting is a blocking operation, so call setblocking()
# after it returns.
server_address = ("192.168.0.100", 1234) #Enter Raspberry's IP
print('connecting to {} port {}'.format(*server_address))
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
######---SSL part for TCP Socket connection----####
sock=ssl.wrap_socket(s_sock, ca_certs="/home/rajib/Project_CAP6133/ca.crt", cert_reqs=ssl.CERT_REQUIRED)
########------End of SSL part for TCP Socket connection------------####
sock.connect(("192.168.0.100", 1234))#Enter Raspberry's IP
sock.setblocking(False)

# Set up the selector to watch for when the socket is ready
# to send data as well as when there is data to read.
mysel.register(
    sock,
    selectors.EVENT_READ | selectors.EVENT_WRITE,
)

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print('client({})'.format(client_address))

        if mask & selectors.EVENT_READ:
            print('  ready to read')
            data = connection.recv(1024)
            if data:
                # A readable client socket has data
                print('  received {!r}'.format(data))
                bytes_received += len(data)

            # Interpret empty result as closed connection,
            # and also close when we have received a copy
            # of all of the data sent.
            keep_running = not (
                data or
                (bytes_received and
                 (bytes_received == bytes_sent))
            )

        if mask & selectors.EVENT_WRITE:
            print('  ready to write')
            if not outgoing:
                # We are out of messages, so we no longer need to
                # write anything. Change our registration to let
                # us keep reading responses from the server.
                print('  switching to read-only')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                # Send the next message.
                #next_msg = outgoing.pop()
		#########################################################
		print ("ENTER THE START (MHz) AND END (MHz) FREQUENCY YOU WANT TO SCAN\n") 
		print ("PRESS CTRL + C WHEN YOU WANT TO STOP\n") 

		while True:
			freq = int(raw_input("Enter Start Frequncy (MHz): "))
			channel_bw = int(raw_input("Enter End Frequency (MHz): "))
			sep = ' '
			next_msg = str(freq) + sep + str(channel_bw) + sep # sep = ' ' or sep = `\n`
		#########################################################
               		print('  sending {!r}'.format(next_msg))
                	sock.sendall(next_msg)
                	bytes_sent += len(next_msg)

print('shutting down')
mysel.unregister(connection)
connection.close()
mysel.close()
