import os 
import time  

secunde = input("cate secunde doriti")

def progress_bar(secunde): 
	for progress in range(0, secunde - 1): 
		procentaj = (progress * 100) // secunde 
		print("Loading...") 
		print("<" +  ("=" * progress) + ((" ") * (secunde - progress)) + ">" + str(procentaj) + "%") 
		print("\n") 
		time.sleep(1)  
		os.system('clear') 
		if (procentaj == 100):  
			time.sleep(1) 
			break  

progress_bar(secunde)
print("Gata")
