import random
from utils import moduloDe

class Game:
    def __init__(self, probabilidadeA):
        self.probabilidadeA = probabilidadeA
        self.pontos = {
            "A": "0",
            "B": "0"
        }
        self.roundsJogados = 0
        self.vencedor = None

    def joga_game(self):
        while self.vencedor == None:
            self.joga_round()
            print(f"{self.pontos['A']}-{self.pontos['B']}")

    def joga_round(self):
        resultado = random.uniform(0, 1)

        if resultado < self.probabilidadeA:
            self.ganha_A()
        else:
            self.ganha_B()

        self.roundsJogados += 1
  
    def ganha_A(self):
        if self.pontos["A"] == '0':
            self.pontos["A"] = '15'
            self.pontos["B"] = 'Love'
        elif self.pontos["A"] == '15' and self.pontos["B"] != '30' and self.pontos["B"] != '40':
            self.pontos["A"] = '30'
        elif self.pontos["A"] == '30':
            self.pontos["A"] = '40'
        elif self.pontos["A"] == '40' or self.pontos["A"] == 'Adv A':
            self.pontos["A"] = 'A wins'
            self.pontos["B"] = 'A wins'
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
        elif self.pontos["B"] == '40' or self.pontos["B"] == 'Adv B':
            self.pontos["A"] = 'B wins'
            self.pontos["B"] = 'B wins'
            self.vencedor = 'B'
        elif self.pontos["B"] == 'Love':
            self.pontos["B"] = '15'
        elif (self.pontos["B"] == '15' and self.pontos["A"] == '30') or self.pontos["A"] == 'Adv A':
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
        self.setRounds = 0
        self.gamesJogados = 0
        self.vencedor = None
    
    def joga_set(self):
        # Para vencer o set ou algum chega a 6 pontos com 2+ de diferença ou são jogados 13 jogos
        while (((moduloDe(self.pontos['A'] - self.pontos['B'])>=2) & ((self.pontos['A'] == 6) | (self.pontos['B'] == 6))) == False) & (self.gamesJogados < 13)  :
            game = Game(self.probabilidadeA)

            print(f"\nGame {self.gamesJogados}:")
            game.joga_game()

            self.pontos[game.vencedor] += 1            
            self.gamesJogados += 1
            self.setRounds += game.roundsJogados
        
        print(f"\nA: {self.pontos['A']} || B: {self.pontos['B']}")
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
        self.totalGames = 0
        self.totalRounds = 0
        self.vencedor = None
    
    def joga_partida(self):
        while ((self.setsGanhos["A"] != 2) & (self.setsGanhos["B"] != 2)):
            set = Set(self.probabilidadeA)
            
            print(f"Iniciando Set {self.setsJogados+1}:")

            set.joga_set()

            print(f"\n=== Vencedor do set {self.setsJogados+1}: {set.vencedor}\n")

            self.setsGanhos[set.vencedor] += 1
            self.setsJogados += 1
            self.totalGames += set.gamesJogados
            self.totalRounds += set.setRounds

        # Define o vencedor da partida
        if self.setsGanhos["A"] > self.setsGanhos["B"]:
            self.vencedor = "A"
        else: 
            self.vencedor = "B"
