import wolframalpha 

da = input("Esti gata sa pui o intrebare?")
while da == "da":
	Intrebare = input("Intrebare: ") 
	app_id = "UX8XJX-373G2XJ8QH" 
	client = wolframalpha.Client(app_id)

	res = client.query(Intrebare) 
	answer = next(res.results).text 

	print("Raspunsul este:" + answer)

	da = input("Mai vrei sa pui o intrebare?")