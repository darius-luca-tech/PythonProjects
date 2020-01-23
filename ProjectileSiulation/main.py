import pygame 
import math 


wScren = 1200 
hScreen = 500 

win = pygame.display.set_mode((wScren, hScreen)) 
pygame.display.set_caption("Simulare") 

class minge(object): 
	def __init__(self, x, y ,radian, culoare): 
		self.x = x
		self.y = y 
		self.radian = radian 
		self.culoare = culoare 
		
	def draw(self, win): 
		pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radian) 
		pygame.draw.circle(win, self.culoare, (self.x, self.y), self.radian - 1) 

	@staticmethod 
	def traiectorie_minge(startx, starty, putere, unghi, timp): 
		velx = math.cos(unghi) * putere
		vely = math.sin(unghi) * putere

		distX = velx * timp 
		distY = (vely * timp) + ((-4.9 * (timp ** 2)) / 2) 

		newx = round(distX + startx) 
		newy = round(starty - distY) 

		return (newx, newy)

def refresh(): 
	win.fill((64, 64, 64)) 
	minge_a.draw(win) 
	pygame.draw.line(win, (0, 0, 0), line[0], line[1]) 
	pygame.display.update() 

def unghi_gasire(pos): 
	sX = minge_a.x 
	sY = minge_a.y 

	try: 
		unghi = math.atan((sY - pos[1]) / (sX - pos[0])) 
	except: 
		unghi = math.pi / 2

	if pos[1] < sY and pos[0] > sX: 
		unghi = abs(unghi) 
		print(unghi) 
	elif pos[1] < sY and pos[0] < sX: 
		unghi = math.pi - unghi 
		print(unghi) 
	elif pos[1] > sY and pos[0] < sX: 
		unghi = math.pi + abs(unghi) 
		print(unghi)
	elif pos[1] > sY and pos[0] > sX: 
		unghi = (math.pi * 2) - angle 
		print(unghi)


	return unghi 

minge_a = minge(300, 494, 5, (255, 255, 255)) 
print(minge_a)
run = True 
timp = 0 
putere = 0 
unghi = 0 
actionare_minge = False 
Ceas = pygame.time.Clock() 
while run: 
	Ceas.tick(200) 
	if actionare_minge: 
		if minge_a.y < 500 - minge_a.radian: 
			timp += 0.05 
			po = minge.traiectorie_minge(x, y, putere, unghi, timp) 
			minge_a.x = po[0] 
			minge_a.y = po[1] 
		else: 
			actionare_minge = False 
			timp = 0 
			minge_a.y = 494 

	line = [(minge_a.x, minge_a.y), pygame.mouse.get_pos()] 
	refresh() 

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False 

		if event.type == pygame.MOUSEBUTTONDOWN: 
			if not actionare_minge: 
				x = minge_a.x 
				y = minge_a.y 
				pos = pygame.mouse.get_pos() 
				actionare_minge = True 
				putere = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][1]) ** 2) / 8 
				print(putere)
				unghi = unghi_gasire(pos)  
				print(pos)

pygame.quit() 
quit() 

