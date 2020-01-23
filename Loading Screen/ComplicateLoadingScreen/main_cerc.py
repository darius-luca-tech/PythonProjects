from time import sleep 
import cerc2 as start 

start.set_text("Incepem in 3") 
start.seteaza_cadre(["-", "/", "\\"])
start.set_culoare_text("red") 
start.culoarea_cercului("green")   
start.start()
sleep(1) 

start.set_text("Incepem in 2") 
start.set_culoare_text("red") 
start.culoarea_cercului("green") 
start.start() 
sleep(1) 

start.set_text("Incepem in 1") 
start.set_culoare_text("red") 
start.culoarea_cercului("green") 
start.start()  
sleep(1)

start.set_text("Ignition")  
start.set_culoare_text("red") 
start.culoarea_cercului("green") 
start.start() 
sleep(3) 

start.set_text("Lift off, going to space") 
start.set_culoare_text("magenta") 
start.culoarea_cercului("green")
sleep(4) 
start.stop() 
print("")
