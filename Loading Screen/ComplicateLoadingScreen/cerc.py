from time import sleep 
import threading 

cadre = ["\u005F", "\u23B8", "\u203E", "\u23B9"] 
check = False 
running = False 
text = "Made by Luca Cristea" 
culoare_text = "" 
culoare_cerc = "" 
restart = "" 

def __init__(self): 
	return self 

def stop_verificare(): 
	return check 

def cadre_(): #get framers
	return cadre 

def seteaza_cadrele(frames): 
	cadre = frames 

def stop(): 
	check = True 

def get_text(): 
	return text 

def culoarea_textului(): 
	return culoare_text 

def culoarea_cercului(): 
	return culoare_cerc 

def cerc(): 
	text = get_text() 
	cadre = cadre_() 
	culoare_text = culoarea_textului() 
	culoare_cerc = culoarea_cercului() 
	frame = 1 
	while not stop_verificare():  
		print("\r \u001b[2K" + culoare_cerc + cadre[(frame - 1) % len(cadre)] + " " + restart + culoare_text + text + restart,end="",flush = True) 
		frame = frame + 1 
		sleep(0.1) 
		text = get_text() 
		culoare_text = culoarea_textului() 
		culoare_cerc = culoarea_cercului() 
		if(frame - 1) % len(cadre) == 0: 
			cadre = cadre_() 
			frame = 1 

	print("") 

def start(): 
	if running: 
		return None 

	spin_obiect = threading.Thread(target = cerc) 
	spin_obiect.start() 

def demo(): 
	try: 
		start() 
	except KeyboardInterrupt: 
		print("") 

if __name__ == "__main__": 
	demo()