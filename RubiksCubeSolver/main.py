from sys import exit as Kill 
try: 
	import sys 
	import kociemba 
	import argparse 

	from combiner import combine 
	from video import webcam 
	from normalizer import normalize 
except ImportError as err: 
	Kill(err) 

class Qbr: 
	def __init__(self, normalize, language): 
		self.humanize = normalize 
		self.language = (language[0]) if isinstance(language, list) else language 

	def run(self):  
		state = webcam.scan() 
		if not state: 
			print('\033[0;33m[QBR SCAN ERROR] Ops, you did not scan in all 6 sides.') 
			print('Please try again.\033[0m') 
			Kill(1) 

		unsolvedState = combine.sides(state) 
		try: 
			algorithm = kociemba.solve(unsolvedState) 
			length = len(algorithm.split(' ')) 
		except Exception as err: 
			print('\033[0;33m[QBR SOLVE ERROR] Ops, you did not scan in all 6 sides correctly.') 
			print('Please try again. \033[0m') 
			Kill(1)  

		print("Solution is:") 
		print('Starting position:') 
		print(algorithm, '({0} moves)'.format(length), '\n') 

		if self.humanize: 
			manual = normalize.algorithm(algorithm, self.language) 
			for index, text in enumerate(manual): 
				print('{}, {}'.format(index+1, text)) 
		Kill(0) 

if __name__ == '__main__': 
	ap = argparse.ArgumentParser() 
	ap.add_argument('-n', '--normalize', default = False, action = 'store_true', 
					help = "Helps") 
	ap.add_argument('-l', '--language', nargs = 1, default = 'en', 
					help = "Languges en | n")  
	args = ap.parse_args() 

	Qbr( 
		args.normalize, 
		args.language
	).run()


		
