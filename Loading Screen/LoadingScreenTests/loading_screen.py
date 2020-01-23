import pygame 
import random 
import time

pygame.init() 
black = [0, 0, 0] 
green = [0, 255, 0] 

smallfont = pygame.font.SysFont("comicsans", 25) 
print(pygame.font.get_fonts())

display_width = 1050 
display_height = 500 

size = [display_width, display_height] 
screen = pygame.display.set_mode(size) 

clock = pygame.time.Clock() 

progress = 0 	

def text_objects(text, color, size): 
	if size == "small": 
		text_surface = smallfont.render(text, True, color) 
	return text_surface, text_surface.get_rect() 

def loading(progress): 
	if progress < 100: 
		text = smallfont.render("Ma incarc fraiere:" + str(int(progress)) + "%", True, green) 
	else: 
		text = smallfont.render("Ma incarc fraiere:" + str(100) + "%", True, green) 

	screen.blit(text, [453, 273]) 
     
def message_to_screen(msg, color, y_displace = 0, size = "small"): 
	textSurf, textRect = text_objects(msg, color, size) 
	textRect.center = (display_width / 2), (display_height / 2) + y_displace 
	screen.blit(textSurf, textRect) 

def main():
while (progress / 2) < 100:
	time_count = (random.randint(1, 1)) 
	increase = random.randint(1, 20) 
	progress += increase  
	screen.fill(black) 
	pygame.draw.rect(screen, green, [423, 223, 204, 49]) 
	pygame.draw.rect(screen, black, [424, 224, 202, 47]) 
	if (progress / 2) > 100: 
		pygame.draw.rect(screen ,green, [425, 225, 200, 45])  
	else: 
		pygame.draw.rect(screen, green, [425, 225, progress, 45]) 

	loading(progress / 2) 
	pygame.display.flip() 

	time.sleep(time_count)




	 

