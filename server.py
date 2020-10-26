# Server.py

import socket
import sys
from thread import *

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print ('Socket bind complete')

#Start listening on socket
s.listen(10)
print ('Socket now listening')

#Function for handling connections. This will be used to create threads
def clientthread(conn):
	#Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
	
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		
		#Receiving from client
		data = conn.recv(1024)
		reply = 'OK...' + data
		if "!q" in data:
			print("!q in data")
			conn.close()

		if "!sendall" in data:
			sendallClients(data[9:])
   
		if not data: 
			break
	
		conn.sendall(reply)
	
	#came out of loop
	conn.close()


def sendallClients(message):
    for client in clients_list:
        client.send(message)
        
clients_list = []

#now keep talking with the client
while 1:
    #global clients_list
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	clients_list.append(conn)
	print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientthread ,(conn,))

s.close()