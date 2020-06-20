import pygame 
import Tkinter 
import time 
import random 
import sys 

pygame.init() 

bg = pygame.image.load("background/testing/monsterBG/bg.png") 
rpsInstW = [pygame.image.load("monsters/rps/rock.jpg"), pygame.image.load("monsters/rps/paper.jpg"), pygame.image.load("monsters/rps/scissors.jpg")] 
rpsInstB = [pygame.image.load("monsters/rps/rock2.jpg"), pygame.image.load("monsters/rps/paper2.jpg"), pygame.image.load("monsters/rps/scissors2.jpg")] 
font = pygame.font.SysFont("Ariel", 50) 
sleepTime = 1.5 

LoseCare = [pygame.image.load("scares/a.jpg"), pygame.image.load("scares/b.jpg"), pygame.image.load("scares/c.jpg"), pygame.image.load("scares/d.jpg"), pygame.image.load("scares/e.jpg"), pygame.image.load("scares/f.jpg"), pygame.image.load("scares/g.jpg")] 

def dialog(display, Self, Oppo, result, scrX, scrY): 
    label = font.render("Tu ai ales" + Self, 1, (255, 255, 255))
    label2 = font.render("Oponentul a ales" + Oppo, 1, (255, 255, 255)) 
    label3 = font.render(result, 1, (255, 255, 255)) 

    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
    display.blit(label, (50, scrY - 190)) 
    pygame.display.update() 
    time.sleep(sleepTime) 

    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
    display.blit(label2, (50, scrY - 190)) 
    pygame.display.update() 
    time.sleep(sleepTime) 

    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
    display.blit(label3, (50, scrY - 190)) 
    pygame.display.update() 
    time.sleep(sleepTime) 

    if result == "Ai pierdut, acum ai sa imi infrunti moartea" or result == "Egal, tot ai sa infrunti moartea": 
        scare = random.randint(0, 3) 
        display.blit(LoseCare[scare], (0, 0)) 
        pygame.display.update() 
        time.sleep(.5) 


def WinsauMori(char, oppo): 
    if char == oppo: 
        result = "Egal, tot ai sa infrunti moartea" 
    elif char + 1 == oppo or char - 2 == oppo: 
        result = "Ai pierdut, acum ai sa imi infrunti moartea" 
    elif oppo + 1 == char or oppo - 2 == char: 
        result = "Ai castigat, norocosule" 
    
    return result 

def MonsterMeet(name, Mstats, Minst, Chealth, Cbd, Cinv, CitemStats, scrX, scrY, display): 
    Chp = Chealth 
    Mhealth = Mstats[0] 
    over = 0 
    result2 = 2 
    rpsCoor = [[12, scrY - 200], [294, scrY - 200], [576, scrY - 200]] 
    for i in range(4): 
        pygame.draw.rect(display, (0, 0,0 ), (0, 0, scrX, scrY)) 
        pygame.display.update() 
        time.sleep(0.1) 
        pygame.draw.rect(display, (255, 255, 255), (0, 0, scrX, scrY)) 
        time.sleep(0.1) 
    
    label = font.render("Uite-l pe " + name + "!" , 1, (255, 255, 255)) 
    display.blit(bg, (0, 0)) 
    display.blit(Minst, (400, 300)) 
    pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY))  
    display.blit(label, (50, scrY - 190))
    pygame.display.update() 
    time.sleep(sleepTime) 
    rpsWBlit = [1, 0, 0] 

    while over != 1: 
        Cchoice = 0 
        while Cchoice == 0:
            time.sleep(.1)
            for event in pygame.event.get(): 
                if event.type == pygame.locals.QUIT: 
                    pygame.quit() 
                    sys.exit() 
            
            keys = pygame.key.get_pressed() 
            if keys[pygame.K_RIGHT]: 
                nextW = rpsWBlit.index(1) + 1 
                rpsWBlit[nextW - 1] = 0 
                if nextW == 3: 
                    nextW = 0 
                rpsWBlit[nextW] = 1 
            
            elif keys[pygame.K_LEFT]: 
                nextW = rpsWBlit.index(1) - 1 
                rpsWBlit[nextW + 1] = 0 
                if nextW == -1: 
                    nextW = 2 
                rpsWBlit[nextW] = 1
            
            elif keys[pygame.K_e]: 
                CchoiceN = rpsWBlit.index(1) 
                if CchoiceN == 0: 
                    Cchoice = "Piatra" 
                elif CchoiceN == 1: 
                    Cchoice = "Hartie" 
                elif CchoiceN == 2: 
                    Cchoice = "Foarfece" 
            
            pygame.draw.rect(display, (0, 0, 0) , (0, scrY - 200, scrX, scrY)) 

            for index, a in enumerate(rpsWBlit): 
                if rpsWBlit[index] == 1: 
                    display.blit(rpsInstW[index], rpsCoor[index]) 
                else: 
                    display.blit(rpsInstB[index], rpsCoor[index]) 
            
            pygame.display.update() 
        MchoiceN = random.randint(0, 2) 
        if MchoiceN == 0: 
            Mchoice = "Piatra" 
        elif MchoiceN == 1: 
            Mchoice = "Hartie" 
        elif MchoiceN == 2: 
            Mchoice = "Foarfece"  
        
        result = WinsauMori(CchoiceN, MchoiceN) 
        dialog(display, Cchoice, Mchoice, result, scrX, scrY) 
        bigest = 0 
        if result == "Ai castigat, norocosule!": 
            if len(CitemStats) != 0: 
                Mhealth -= Cbd + int(CitemStats[-1]) 
            else: 
                Mhealth -= Cbd 
        
        elif result == "Ai pierdut, acum ai sa imi infrunti moartea": 
            Chp -= Mstats[1] 
        elif result == "Egal, tot ai sa infrunti moartea": 
            Chp -= 20  
            Mhealth -= 20 
        
        display.blit(bg, (0, 0)) 
        display.blit(Minst, (400, 300)) 
        if result == "Ai castigat, norocosule!": 
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
            label3 = font.render("Ai atacat cu " + Cinv[bigest], 1, (255 ,255, 255)) 
            display.blit(label3, (50, scrY - 190)) 
            pygame.display.update() 
        
        time.sleep(sleepTime) 
        pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
        label4 = font.render("Health percent: " + str(Chp) + ", " + "'s health percent " + str(Mhealth), 1, (255, 255, 255)) 
        display.blit(label4, (50, scrY - 190)) 
        pygame.display.update() 
        time.sleep(sleepTime) 
        if Mhealth <= 0: 
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
            label5 = font.render("Asa am exterminat-o si eu pe ma-ta ", 1, (255, 255, 255)) 
            display.blit(label5, (50, scrY - 190)) 
            pygame.display.update() 
            time.sleep(sleepTime) 
            over = 1 
            result2 = 1 
        
        elif Chp <= 0: 
            pygame.draw.rect(display, (0, 0, 0), (0, scrY - 200, scrX, scrY)) 
            label6 = font.render("Ti-ai luat-o fraiere ", 1, (255, 255, 255)) 
            display.blit(label6, (50, scrY - 190)) 
            pygame.display.update() 
            time.sleep(sleepTime) 
            over = 1 
            result = 0 
    
    return result2
