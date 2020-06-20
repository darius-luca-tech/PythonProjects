from sys import exit as Kill 
try: 
	import sys 
	import json 
except importError as err: 
	Kill(err) 

class Normalizer: 
	def algorthm(self, alg, language): 
		with open('solve-manual.json') as f: 
			manual = json.load(f) 

		solution = [] 
		for notation in alg.split(' '): 
			solution.append(manual[language][notation]) 
		return solution 

normalize = Normalizer()