import cerc 
try: 
	from colorama import Fore 
	cerc.restart = Fore.RESET 
except: 
	pass 

def set_text(text): 
	cerc.text = text 

def seteaza_cadre(frames): 
	cerc.cadre = frames 

def start(): 
	cerc.stop = False 
	cerc.start() 

def stop(): 
	cerc.check = True 

def Dict_culori(color): 
	color = color.lower() 
	if color == "red": 
		return Fore.RED 
	if color == "green": 
		return Fore.GREEN 
	if color == "black": 
		return Fore.BLACK 
	if color == "yellow": 
		return Fore.YELLOW 
	if color == "magenta":
		return Fore.MAGENTA 
	if color == "cyan": 
		return Fore.CYAN 
	if color == "white": 
		return Fore.WHITE  
	raise Exception("Culoarea" + color + " nu este potrivita")  

def set_culoare_text(color): 
	color = color.lower() 
	if not Fore: 
		raise ImportException("I dont give a fuck about ur work, I will not execute") 
	cerc.culoare_text = Dict_culori(color) 

def culoarea_cercului(color): 
	color = color.lower() 
	if not Fore: 
		raise ImportException("I dont give a fuck about ur work, I will not execute")  

	cerc.culoarea_cerc = Dict_culori(color)  

def FAIL(message): 
	return None
