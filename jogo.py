import random

class Game:
    def __init__(self, probabilidadeA):
        self.probabilidadeA = probabilidadeA
        self.pontos = {
            "A": "0",
            "B": "0"
        }
        self.vencedor = None

    def joga_game(self):
      while self.vencedor == None:
          self.joga_round()

    def joga_round(self):
        resultado = random.uniform(0, 1)

        if resultado <= self.probabilidadeA:
            self.ganha_A()
        else:
            self.ganha_B()
  
    def ganha_A(self):
        if self.pontos["A"] == '0':
            self.pontos["A"] = '15'
            self.pontos["B"] = 'Love'
        elif self.pontos["A"] == '15' and self.pontos["B"] != '30' and self.pontos["B"] != '40':
            self.pontos["A"] = '30'
        elif self.pontos["A"] == '30':
            self.pontos["A"] = '40'
        elif self.pontos["A"] == '40' or self.pontos["A"] == 'Adv A':
            self.pontos["A"] = 'G'
            self.vencedor = 'A'
        elif self.pontos["A"] == 'Love':
            self.pontos["A"] = '15'
        elif (self.pontos["A"] == '15' and self.pontos["B"] == '30') or self.pontos["A"] == 'Adv B':
            self.pontos["A"] = 'Deuce'
            self.pontos["B"] = 'Deuce'
        elif self.pontos["A"] == '15' and self.pontos["B"] == '40':
            self.pontos["A"] = 'Adv B'
            self.pontos["B"] = 'Adv B'
        elif self.pontos["A"] == 'Deuce':
            self.pontos["A"] = 'Adv A'
            self.pontos["B"] = 'Adv A'


    def ganha_B(self):
        if self.pontos["B"] == '0':
            self.pontos["B"] = '15'
            self.pontos["A"] = 'Love'
        elif self.pontos["B"] == '15' and self.pontos["A"] != '30' and self.pontos["A"] != '40':
            self.pontos["B"] = '30'
        elif self.pontos["B"] == '30':
            self.pontos["B"] = '40'
        elif self.pontos["B"] == '40' or self.pontos["B"] == 'Adv A':
            self.pontos["B"] = 'G'
            self.vencedor = 'B'
        elif self.pontos["B"] == 'Love':
            self.pontos["B"] = '15'
        elif (self.pontos["B"] == '15' and self.pontos["A"] == '30') or self.pontos["A"] == 'Adv B':
            self.pontos["A"] = 'Deuce'
            self.pontos["B"] = 'Deuce'
        elif self.pontos["B"] == '15' and self.pontos["A"] == '40':
            self.pontos["A"] = 'Adv A'
            self.pontos["B"] = 'Adv A'
        elif self.pontos["B"] == 'Deuce':
            self.pontos["A"] = 'Adv B'
            self.pontos["B"] = 'Adv B'



class Set:
    def __init__(self, probabilidadeA):
        self.probabilidadeA = probabilidadeA
        self.pontos = {
            "A": 0,
            "B": 0
        }
        self.gamesJogados = 0
        self.vencedor = None
    
    def joga_set(self):
        while self.gamesJogados < 7:
            game = Game(self.probabilidadeA)

            game.joga_game()

            self.pontos[game.vencedor] += 1            
            self.gamesJogados += 1
        
        # Define o vencedor do set
        if self.pontos["A"] > self.pontos["B"]:
            self.vencedor = "A"
        else: 
            self.vencedor = "B"

class Partida:
    def __init__(self, probabilidadeA):
        self.probabilidadeA = probabilidadeA
        self.setsJogados = 0
        self.setsGanhos = {
            "A": 0,
            "B": 0
        }
        self.vencedor = None
    
    def joga_partida(self):
        while self.setsJogados < 3:
            set = Set(self.probabilidadeA)
            
            set.joga_set()

            self.setsGanhos[set.vencedor] += 1
            self.setsJogados += 1

        # Define o vencedor da partida
        if self.setsGanhos["A"] > self.setsGanhos["B"]:
            self.vencedor = "A"
        else: 
            self.vencedor = "B"
