#!/usr/bin/env python3
#clien.py
"""[Lab 4 Description]
    - Create the client and server file
    - Client send requesting messages to server and get back the response from server. 
    - Server get requesting from client and response the message. 
    https://www.binarytides.com/python-socket-programming-tutorial/   
    - Client socket programming
"""
#Socket client example in python

import socket	#for sockets
import sys	#for exit

#create an INET, STREAMing socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()
	
print ('Socket Created')
host = input("host: ")
print('Host name: ' + host)
#host = 'www.google.com';
port = 80;

try:
	remote_ip = socket.gethostbyname( host )

except socket.gaierror:
	#could not resolve
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

#Connect to remote server
s.connect((remote_ip , port))

print ('Socket Connected to ' + host + ' on ip ' + remote_ip)

#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try :
	#Set the whole string
	s.sendall(message.encode('utf-8'))
except socket.error:
	#Send failed
	print ('Send failed')
	sys.exit()

print ('Message send successfully')

#Now receive data
reply = s.recv(4096) 

print (reply)