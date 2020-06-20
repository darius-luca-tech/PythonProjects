class ProgressBar(): 
	def __init__(self, steps = 10): 
		self.steps = steps 
		self.prefix_text = '' 
		self.suffix_text = '' 
		self.caracter_progres = '█' 
		self.fil_char = '░' 
		self.__completed = False 

	def show(self, current_val): 
		if current_val > self.steps:
			self.complete() 
			return  

		progres = '{0:{fill}{align}{length}}'.format(self.caracter_progres * current_val, fill = self.fil_char, align = '<', length = self.steps) 
		percent = '{0:1f}'.format(100 * (current_val / float(self.steps))) 
		bar_text = '{0} | {1} | {2}%| {3}'.format(self.prefix_text, progres, percent, self.suffix_text) 

		print(bar_text, end = '\r') 

	def complete(self, message = '------------> Ready to take off!'):

		if not self.__completed: 
			print() 
			print(message) 
			self.__completed = True