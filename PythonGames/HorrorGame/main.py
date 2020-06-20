import pygame 
from pygame.locals import * 
import sys 
import Mesagge 
import Monster 
import time 
import random 

pygame.init() 

dp = pygame.display.set_mode((1200, 700), 0, 32) 
bg = pygame.image.load("background/testing/bg.jpg") 
items = [pygame.image.load("items/knife.png"), pygame.image.load("items/flamingSword.png")] 
monsters = [pygame.image.load("monsters/a.jpg"), pygame.image.load("monsters/b.png"), pygame.image.load("monsters/c.jpg"), pygame.image.load("monsters/d.jpg")] 
surf = pygame.image.load("surfaces/surf.png") 
jumpscares = [pygame.image.load("scares/a.jpg"), pygame.image.load("scares/b.jpg"), pygame.image.load("scares/c.jpg"), pygame.image.load("scares/d.jpg"), pygame.image.load("scares/e.jpg"), pygame.image.load("scares/f.jpg"), pygame.image.load("scares/g.jpg")] 

itemCoor = [[1500, 430], [3000, 470]] 
itemName = ["Knife", "Flaming Sword"] 
itemStat = ["50", "200"] 
surfCoor = [[1400, 490], [2000, 300]] 
monsName = ["Harpy", "Shiv", "Assasin", "Danut"] 
monsCoor = [[2000, 500], [4000, 500], [6000, 400], [10000, 150]] 
monsStat = [[200, 20], [300, 50], [500, 60], [1000, 80]] 
monsMet = [0, 0, 0, 0] 
surfSize = (200, 30) 
charBaseAttack = 20
charX = 0 
charY = 500 
charHealth = 500 
charBaseHealth = 2
charItem = [] 
charItemStats = [] 
charHeight = 200 
charWidth = 140 
gravity = 10 
velY = 0 
isJumping = False 

bgX = c = counter = over = 0 
moveSpeed = 5 
sleepTime = 2

itemList = [] 

char = [] 
for i in range(1, 9): 
    char.append(pygame.image.load("character/chr" + str(i) + ".jpg")) 

while over != 1: 
    result2 = 2 
    index2 = 0 
    dp.blit(bg, (bgX, 0)) 
    dp.blit(bg, (bgX + 1280, 0)) 
    dp.blit(char[c - 1], (50, charY)) 
    if itemCoor != []: 
        for index, i in enumerate(itemCoor): 
            dp.blit(items[index], (i)) 
    
    for a in surfCoor: 
        dp.blit(surf, a) 
    
    if monsCoor != []: 
        for index, i in enumerate(monsCoor):
            dp.blit(monsters[index], (i)) 

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
    
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_x]: 
        pygame.display.quit() 
        sys.exit() 
    elif keys[K_RIGHT]: 
        charX += moveSpeed 
        bgX -= moveSpeed 
        for index, a in enumerate(surfCoor): 
            surfCoor[index][0] -= moveSpeed 
        for index, b in enumerate(itemCoor): 
            itemCoor[index][0] -= moveSpeed 
        for index, x in enumerate(monsCoor): 
            x[0] -= moveSpeed 
        
        counter += 1 
        if counter >= 5: 
            c += 1 
            counter = 0 
        if c > 8: 
            c = 1
        if bgX <= -1280: 
            bgX = 0 
        
    elif keys[K_LEFT]: 
        if charX - moveSpeed >= 0: 
            charX -= moveSpeed
            bgX += moveSpeed 
            for index, a in enumerate(surfCoor): 
                surfCoor[index][0] += moveSpeed 

            for index, b in enumerate(itemCoor): 
                itemCoor[index][0] += moveSpeed 

            for index, x in enumerate(monsCoor): 
                x[0] += moveSpeed 

            counter += 1
            if counter >= 5:
                c -= 1 
                counter = 0 
            if c < 1: 
                c = 8 
            if bgX >= 0: 
                bgX = -1280 
    elif keys[K_UP]: 
        maxJump = 90 
        if isJumping == False: 
            velY = maxJump 
            isJumping = True 
    
    if isJumping == True: 
        charY -= velY 
        velY -= gravity 
        for x in surfCoor: 
            if x[1] - 50 <= charY + charHeight <= x[1] and (50 <= x[0] <= 50 + charWidth or x[0] <= 50 and 50 + charWidth <= x[0] + surfSize[0] or 50 <= x[0] + surfSize[0] <= 50 + charWidth) and velY < 0: 
                charY = x[1] - charHeight 
                isJumping = False 
        
        if charY >= 500: 
            charY = 500 
            isJumpung = False 
    
    for a in surfCoor: 
        if isJumping == False: 
            if a[1] - 10 <= charY + charHeight <= a[1]  and(a[0] + surfSize[0] < 50 or a[0] > 50): 
                if charY != 500: 
                    isJumping = True 
                    velY = 0 
    
    for index, a in enumerate(itemCoor): 
        if 50 + charWidth > a[0] > 50 and charY + charHeight > a[1] > charY: 
            Mesagge.MakeMessageBox(itemName[index], 1200, 800 ,dp) 
            time.sleep(sleepTime) 
            charItem.append(itemName[index]) 
            charItemStats.append(itemStat[index]) 
            itemCoor.remove(itemCoor[index]) 
            itemName.remove(itemName[index]) 
            itemStat.remove(itemStat[index]) 
            items.remove(items[index]) 
    
    for index, a in enumerate(monsCoor): 
        if a[0] == 50 + charWidth: 
            if monsMet[index] == 0: 
                monsMet[index] = 1
                result = Monster.MonsterMeet(monsName[index], monsStat[index], monsters[index], charHealth, charBaseAttack, charItem, charItemStats, 1200, 800, dp) 
                index2 = index  
            
            if result == 0: 
                whichJS = random.randint(0, 3)
                dp.blit(jumpscares[whichJS], (0, 0)) 
                pygame.display.update() 
                time.sleep(sleepTime) 
                over = 1
            elif result == 1: 
                monsName.remove(monsName[index2]) 
                monsCoor.remove(monsCoor[index2]) 
                monsStat.remove(monsStat[index2]) 
                monsters.remove(monsters[index2]) 
                monsMet.remove(monsMet[index2])

    pygame.display.update()  
sys.exit()
    
