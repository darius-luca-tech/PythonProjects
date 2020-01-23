import wikipedia 

while True: 
	intrebare = input("Intrebare:")  
	informatii = input("Cate propozitii doresti?") 
	wikipedia.set_lang("ro")
	print (wikipedia.summary(intrebare, sentences = informatii))