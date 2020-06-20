import random

tabla = [[" " for i in range(3)] for j in range(3)]
#print('\n'.join(map(str, tabla)))
print(" ")
def teren_joc():
    print(" 0    1    2")
    print(" |    |    |")
    print(" -    -    -")
    print(" " + tabla[0][0] +" | "+ tabla[0][1] +"  | "+ tabla[0][2] +  "  <--0")
    print("---|----|---")
    print("   |    |  ")
    print("  "+tabla[1][0]+"| " + tabla[1][1] + "  | " + tabla[1][2] + "  <--1")
    print("---|----|---")
    print(" " + tabla[2][0] + " | " + tabla[2][1] + "  | " + tabla[2][2] + "  <--2")
teren_joc()

X_O = ['X', 'O']
semn_player_1 = random.choice(X_O)
semn_player_2 = random.choice(X_O)
while((semn_player_1 == 'X' and semn_player_2 == 'X') or (semn_player_1 == 'O' and semn_player_2 == 'O')):
     semn_player_1 = random.choice(X_O)
     semn_player_2 = random.choice(X_O)

print(" ")
print("Jucatorul_1 va juca cu {} , iar cu jucatorul_2 va juca cu {}".format(semn_player_1, semn_player_2))
print(" ")

castig = 0
while True:

    mutare_player_1_rand = int(input("<Player 1>---Mentionati numarul randului de la 0 la 2 inclusiv:"))
    mutare_player_1_coloana = int(input("<PLayer 1>---Mentionati numarul coloanei de la 0 la 2 inclusiv:"))
    if(tabla[mutare_player_1_rand][mutare_player_1_coloana] != " " or (mutare_player_1_rand or mutare_player_1_coloana) > len(tabla)):
        print("<Player 1>---Mentionati o pozitie neocupata si o pozitie valida")
        mutare_player_1_rand = int(input("<Player 1>---Mentionati numarul randului de la 0 la 2 inclusiv:"))
        mutare_player_1_coloana = int(input("<Player 1>---Mentionati numarul coloanei de la 0 la 2 inclusiv:"))
    else:
        tabla[mutare_player_1_rand][mutare_player_1_coloana] = semn_player_1
        teren_joc()

    for j in range(3):
        if (tabla[0][j] == tabla[1][j] and tabla[1][j] == tabla[2][j]):
            if(tabla[0][j] == semn_player_1):
                print("Player 1 a castigat!")
                break

            elif(tabla[0][j] == semn_player_2):
                 print("PLayer 2 a castigat")
                 break

    #print(tabla[0][0], tabla[1][1], tabla[2][2])
    if(tabla[0][0] == tabla[1][1] and tabla[1][1] == tabla[2][2]):
        if(tabla[0][0] == semn_player_1):
            print("Player 1 a castigat!")
            break
        elif(tabla[0][0] == semn_player_2):
            print("Player 2 a castigat!")
            break

    for i in range(3):
        if(tabla[i][0] == tabla[i][1] and tabla[i][1] == tabla[i][2]):
            if(tabla[i][0] == semn_player_1):
                print("Player1 a castigat")
                break
            elif(tabla[i][0] == semn_player_2):
                print("Player2 a castigat")
                break
    draw=0
    for i in range(3):
        for j in range(3):
            if(tabla[i][j] != " "):
                draw+=1
    if(draw==9):
        print("Egal")
        break

    mutare_player_2_rand = int(input("<Player 2>---Mentionati numarul randului de la 0 la 2 inclusiv:"))
    mutare_player_2_coloana = int(input("<PLayer 2>---Mentionati numarul coloanei de la 0 la 2 inclusiv:"))
    if(tabla[mutare_player_2_rand][mutare_player_2_coloana] != " " or (mutare_player_2_rand or mutare_player_2_coloana) > len(tabla)):
        print("<Player 2>---Mentionati o pozitie neocupata si o pozitie valida")
        mutare_player_2_rand = int(input("<Player 2>---Mentionati numarul randului de la 0 la 2 inclusiv:"))
        mutare_player_2_coloana = int(input("<Player 2>---Mentionati numarul coloanei de la 0 la 2 inclusiv:"))
    else:
        tabla[mutare_player_2_rand][mutare_player_2_coloana] = semn_player_2
        teren_joc()

    for j in range(3):
        if (tabla[0][j] == tabla[1][j] and tabla[1][j] == tabla[2][j]):
            if(tabla[0][j] == semn_player_1):
                print("Player 1 a castigat!")
                break

            elif(tabla[0][j] == semn_player_2):
                 print("PLayer 2 a castigat")
                 break

    #print(tabla[0][0], tabla[1][1], tabla[2][2])
    if(tabla[0][0] == tabla[1][1] and tabla[1][1] == tabla[2][2]):
        if(tabla[0][0] == semn_player_1):
            print("Player 1 a castigat!")
            break
        elif(tabla[0][0] == semn_player_2):
            print("Player 2 a castigat!")
            break

    for i in range(3):
        if(tabla[i][0] == tabla[i][1] and tabla[i][1] == tabla[i][2]):
            if(tabla[i][0] == semn_player_1):
                print("Player1 a castigat")
                break
            elif(tabla[i][0] == semn_player_2):
                print("Player2 a castigat")
                break
    draw=0
    for i in range(3):
        for j in range(3):
            if(tabla[i][j] != " " and castig == 0):
                draw+=1
    if(draw==9):
        print("Egal")
        break
