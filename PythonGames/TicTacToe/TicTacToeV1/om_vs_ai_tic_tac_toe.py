from math import inf as infinity
from random import choice 
import platform 
import time 
from os import system 

jucator = -1 
AI = +1 
placa = [[0,0,0], 
         [0,0,0],
         [0,0,0]] 

def evalueza(statut): 
    if castig(statut, AI): 
        score = +1 
    elif castig(statut, jucator): 
        score = -1 
    else: 
        score = 0 
    
    return score

def castig(statut, player):
    conditie_castig = [[statut[0][0], statut[0][1], statut[0][2]], 
                       [statut[1][0], statut[1][1], statut[1][2]], 
                       [statut[2][0], statut[2][1], statut[2][2]], 
                       [statut[0][0], statut[1][0], statut[2][0]], 
                       [statut[0][1], statut[1][1], statut[2][1]], 
                       [statut[0][2], statut[1][2], statut[2][2]], 
                       [statut[0][0], statut[1][1], statut[2][2]], 
                       [statut[2][0], statut[1][1], statut[0][2]]] 
    if [player, player, player] in conditie_castig: 
        return True 
    else: 
        return False

def joc_incheiat(statut): 
    return castig(statut, jucator) or castig(statut, AI) 

def celule_goale(statut): 
    cells = [] 

    for x, row in enumerate(statut): 
        for y, cell in enumerate(row): 
            if cell == 0: 
                cells.append([x, y]) 
    
    return cells 

def mutare_corecta(x, y): 
    if [x, y] in celule_goale(placa):
        return True 
    else: 
        return False 

def mutare(x, y, player): 
    if mutare_corecta(x, y): 
        placa[x][y] = player 
        return True 
    else: 
        return False 

def minimax(statut, depth, player): 
    if player == AI: 
        best = [-1, -1, -infinity]  
    else: 
        best = [-1, -1, +infinity] 
    
    if depth == 0 or joc_incheiat(statut): 
        score = evalueza(statut) 
        return [-1, -1, score] 
    
    for cell in celule_goale(statut): 
        x, y = cell[0], cell[1] 
        statut[x][y] = player
        score = minimax(statut, depth - 1, -player) 
        statut[x][y] = 0 
        score[0], score[1] = x, y 

        if player == AI: 
            if score[2] > best[2]: 
                best = score 
        else: 
            if score[2] < best[2]: 
                best = score 
    
    return best 

def clean(): 
    system('clear') 

def placa_show(statut, c_alegere, o_alegere): 
    chars = { 
        -1:o_alegere, 
        +1:c_alegere, 
        0: ' '
    } 

    linie = '-----------------' 

    print('\n' + linie) 
    for row in statut: 
        for cell in row: 
            simbol = chars[cell] 
            print(f'| {simbol} |', end='') 
        print('\n' + linie) 
def miscare_ai(c_alegere, o_alegere): 
    #c_alegere: alegerea calculatorului X si 0
    #o_alegere: alegerea omului X si 0

    depth = len(celule_goale(placa)) 
    if depth == 0 or joc_incheiat(placa):
        return 
    
    clean() 
    print(f'AI alege [{c_alegere}]') 
    placa_show(placa, c_alegere, o_alegere) 

    if depth == 9: 
        x = choice([0, 1, 2]) 
        y = choice([0, 1, 2]) 
    else: 
        move = minimax(placa, depth, AI) 
        x, y = move[0], move[1] 
    
    mutare(x , y, AI) 
    time.sleep(1) 

def miscare_player(c_alegere, o_alegere): 
    depth = len(celule_goale(placa)) 
    if depth == 0 or joc_incheiat(placa): 
        return 

    move = -1 
    moves = { 
        1: [0, 0], 2: [0, 1], 3: [0, 2], 
        4: [1, 0], 5: [1, 1], 6: [1, 2], 
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    } 

    clean() 
    print(f'Randul tau [{o_alegere}]') 
    placa_show(placa, c_alegere, o_alegere) 

    while move < 1 or move > 9: 
        try: 
            move = int(input('1-9:')) 
            coord = moves[move] 
            true_mutare = mutare(coord[0], coord[1], jucator) 
            print(coord[0], coord[1])
            if not true_mutare: 
                print("Pozitie invalida!") 
                move = -1 
        
        except (EOFError, KeyboardInterrupt): 
            print("HA GAY") 
            exit() 
        except(KeyError, ValueError): 
            print("HA GAY") 

def main(): 
    clean() 
    o_alegere = '' 
    c_alegere = '' 
    prima_mutare = ' ' 

    while o_alegere != 'O' and o_alegere != 'X': 
        try: 
            print('') 
            o_alegere = input('X/O:').upper() 
        except(EOFError, KeyboardInterrupt): 
            print("HA GAY") 
            exit() 
        except(KeyError, ValueError): 
            print("HA GAY")  
    
    if o_alegere == 'X': 
        c_alegere = 'O' 
    else: 
        c_alegere = 'X' 
    print(c_alegere)
    #clean() 

    while prima_mutare != 'Y' and prima_mutare != 'N': 
        try: 
            prima_mutare = input("Vrei sa incepi tu?:").upper() 
        except (EOFError, KeyboardInterrupt): 
            print("HA GAY") 
            exit() 
        except (KeyError, ValueError): 
            print("HA GAY")
    
    while len(celule_goale(placa)) > 0 and not joc_incheiat(placa): 
        if prima_mutare == 'N': 
            miscare_ai(c_alegere, o_alegere) 
            prima_mutare = '' 

        miscare_player(c_alegere, o_alegere)
        miscare_ai(c_alegere, o_alegere)

    if castig(placa, jucator): 
        clean() 
        print(f'Ai mutat [{o_alegere}]') 
        placa_show(placa, c_alegere, o_alegere) 
        print("Ai castigat, sper sa nu o mai faci vreodata") 
    elif castig(placa, AI): 
        clean() 
        print(f'AI-ul a pus [{c_alegere}]') 
        placa_show(placa, c_alegere, o_alegere) 
        print("AI-ul a castigat") 
    else: 
        clean() 
        placa_show(placa, c_alegere, o_alegere) 
        print("Egal") 
        

    
    exit() 

if __name__ == '__main__': 
    main()
