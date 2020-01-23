import wikipedia 
import wolframalpha 

 
while True: 
	intrebare = input("Intrebare:")  
	try: 
			app_id = "UX8XJX-373G2XJ8QH" 
			client = wolframalpha.Client(app_id)

			res = client.query(intrebare) 
			answer = next(res.results).text 

			print("Raspunsul este:" + answer)

	except:  
		randuri = input("Cate randuri doriti?")
		wikipedia.set_lang("ro") 
		print(wikipedia.summary(intrebare, senteces = randuri)) 
		
