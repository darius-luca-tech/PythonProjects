#coding: utf-8
from tkinter import *  
from tkinter.font import Font
from copy import deepcopy  

class Tabla_Joc: 
    def __init__(self, other = None): 
        self.player = 'X' 
        self.AI = 'O' 
        self.gol = '-'
        self.marime_tabla = 3
        self.patrate = {} 
        for y in range(self.marime_tabla): 
            for x in range(self.marime_tabla): 
                self.patrate[x, y] = self.gol 
        #__dict__: Un dicționar sau un alt obiect de mapare folosit pentru a stoca atributele unui obiect (redactabile). 
        if other: 
            self.__dict__ = deepcopy(other.__dict__) 
    
    def mutare(self, x, y): 
        placa = Tabla_Joc(self) 
        placa.patrate[x, y] = placa.player
        (placa.player, placa.AI) = (placa.AI, placa.player) 
        return placa 

    def minimax(self, player): 
        #max node 
        if self.castig(): 
            if player: 
                return (-1, None) 
            else: 
                return (+1, None) 
        elif self.egal(): 
            return (0, None) 
        elif player: 
            max = (-2, None) 
            for x, y in self.patrate: 
                if self.patrate[x, y] == self.gol: 
                    inv_om = not player
                    val = self.mutare(x, y).minimax(inv_om)[0] 
                    if val > max[0]: 
                        max = (val, (x, y))  

            return max 

        #min node 
        else: 
            min = (+2, None) 
            for x, y in self.patrate: 
                if self.patrate[x, y] == self.gol: 
                    inv_om = not player
                    val = self.mutare(x, y).minimax(inv_om)[0] 
                    if val < min[0]: 
                        min = (val, (x, y)) 
            return min 
    #Helper for minimax
    def best(self): 
        return self.minimax(True)[1] 
    
    def egal(self): 
        for (x, y) in self.patrate: 
            if self.patrate[x, y] == self.gol: 
                return False 
        return True 
    
    def castig(self): 
        #Orizontal
        for y in range(self.marime_tabla): 
            lista_castig = [] 
            for x in range(self.marime_tabla): 
                if self.patrate[x, y] == self.AI: 
                    lista_castig.append((x, y)) 
            if len(lista_castig) == self.marime_tabla: 
                return lista_castig 
        
        #Vertical 
        for x in range(self.marime_tabla): 
            lista_castig = [] 
            for y in range(self.marime_tabla): 
                if self.patrate[x, y] == self.AI: 
                    lista_castig.append((x, y)) 
            if len(lista_castig) == self.marime_tabla: 
                return lista_castig 
        
        #Diagonala Principala 
        lista_castig = [] 
        for y in range(self.marime_tabla): 
            x = y 
            if self.patrate[x, y] == self.AI: 
                lista_castig.append((x, y)) 
        if len(lista_castig) == self.marime_tabla: 
            return lista_castig 
        
        #Diagonala Secundara 
        lista_castig = [] 
        for y in range(self.marime_tabla): 
            x = self.marime_tabla - 1 - y 
            if self.patrate[x, y] == self.AI: 
                lista_castig.append((x, y)) 
        if len(lista_castig) == self.marime_tabla: 
            return lista_castig  
        else: 
            return None 

class GUI:
    def __init__(self): 
            self.pagina = Tk() 
            self.pagina.title("IA - X&0") 
            self.pagina.resizable(width = True, height = True) 

            self.placa = Tabla_Joc() 
            self.font = Font(family="Helvetica", size = 32) 
            self.butoane = {} 
            self.text = Label(self.pagina, width = 40, height = 10, font = self.font, text='Jocul e deschis, good luck!') 
            self.pagina.config(cursor="pirate") 

            for x, y in self.placa.patrate: 
                cmd = lambda x = x, y = y: self.mutare_gui(x, y)
                buton = Button(self.pagina, command = cmd, font = self.font, width = 2, height = 1) 
                buton.grid(row = y, column = x) 
                self.butoane[x, y] = buton 

            cmd = lambda: self.reset() 
            buton = Button(self.pagina, text='Mai ia-ti o data bataie', command=cmd)
            buton.grid(row = self.placa.marime_tabla + 1, column = 0, columnspan = self.placa.marime_tabla, sticky = "WE") 
            self.text.grid(row = self.placa.marime_tabla + 2, column = 0, columnspan = self.placa.marime_tabla, sticky = "WE") 
            self.updateBoard() 
    
    def reset(self): 
        self.placa = Tabla_Joc() 
        self.updateBoard() 
        if self.text['text'] != ' ': 
            self.text['text'] = ' '
    
    def mutare_gui(self, x, y): 
        self.pagina.config(cursor = "watch") 
        self.pagina.update() 
        self.placa = self.placa.mutare(x, y) 
        self.updateBoard() 
        mutare_gui = self.placa.best() 
        if mutare_gui: 
            self.placa = self.placa.mutare(*mutare_gui) 
            self.updateBoard() 
        self.pagina.config(cursor="pirate") 

    def updateBoard(self): 
        for (x, y) in self.butoane: 
            text = self.placa.patrate[x, y] 
            self.butoane[x, y]['text'] = text 
            if text == self.placa.gol: 
                self.butoane[x, y]['state'] = 'normal' 
            else: 
                self.butoane[x, y]['state'] = 'disabled' 
        
        castigare = self.placa.castig() 
        egal = self.placa.egal() 
        if castigare: 
            self.text['text'] = 'AI-ul a castigat!' 
            for x, y in self.butoane: 
                self.butoane[x, y]['state'] = 'disabled' 
        
        if egal: 
            self.text['text'] = 'Egal! ;(' 
            for x, y in self.butoane: 
                self.butoane[x, y]['state'] = 'disabled' 
        
        for (x, y) in self.placa.patrate: 
            self.butoane[x, y].update() 
    
    def mainloop(self): 
        self.pagina.mainloop() 

if __name__ == '__main__': 
    print("Jocul a inceput, bafta!") 
    GUI().mainloop()