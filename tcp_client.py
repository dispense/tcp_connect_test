#tcp client

import socket

addy = 'www.google.com'
port = 80

# create a socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# af_net is IPv4 addy
	# sock_stream is a TCP client

# connect to client
client .connect((addy, port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# get some data
response = client.recv(4096)

print(response) 