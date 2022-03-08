import random
from utils import moduloDe
from markov import markovWalk

class Game:
    def __init__(self, probabilidadeA):
        self.probabilidadeA = probabilidadeA
        self.roundsJogados = 0
        self.vencedor = None
        self.markovState = "S0" # Estado inicial da cadeia de markov

    def joga_game(self):
        # Enquanto o estado da cadeia de markov nao apontar um vencedor joga um novo round
        while self.markovState != "SWA" and self.markovState != "SWB":
            self.joga_round()

        # Determina vencedor baseado no estado de parada
        if self.markovState == "SWA":
            self.vencedor = "A"
        else:
            self.vencedor = "B"

    def joga_round(self):
        resultado = random.uniform(0, 1)

        if resultado < self.probabilidadeA:
            self.markovState = markovWalk(currentState=self.markovState, diretion=0)
        else:
            self.markovState = markovWalk(currentState=self.markovState, diretion=1)

        self.roundsJogados += 1


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
