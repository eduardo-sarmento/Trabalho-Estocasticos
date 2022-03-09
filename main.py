from jogo import Partida
from jogo import Game
import sys
import pandas as pd

# 1 partida = melhor de 3 sets
# 1 set = melhor de 7 games
# 1 game = cadeia de markov

def resultado(match):
    print(f"======= Vencedor da partida: {match.vencedor}")
    print(f"======= Resultado da partida (A - B):  {match.setsGanhos['A']} - {match.setsGanhos['B']}")
    print(f"======= Todal de Games jogados na partida: {match.totalGames}")
    print(f"======= Todal de Rounds jogados na partida: {match.totalRounds}")


def main():
    n = 30 # Numero de simulacoes por partida
    pA1 = 0.70 # Probabilidade de A na partida 1
    pA2 = 0.45 # Probabilidade de A na partida 2
    
    pA1_Vencedor = []
    pA1_Set_A = []
    pA1_Set_B = []
    pA1_Games = []
    pA1_Rounds = []
    
    pA2_Vencedor = []
    pA2_Set_A = []
    pA2_Set_B = []
    pA2_Games = []
    pA2_Rounds = []
    
    orig_stdout = sys.stdout

    # Abre arquivo da partida 1 e redireciona os prints
    file1_human_readable = open('partida1_human_readable.txt', 'w')
    sys.stdout = file1_human_readable

    # Partida 1: o Jogador A é muito melhor do que o Jogador B
    for i in range(n):
        print(f"-- SIMULACAO {i+1}")
        match = Partida(pA1) 
        match.joga_partida()
        
        resultado(match)
        if match.vencedor == "A":
           pA1_Vencedor.append(1)
        else:
           pA1_Vencedor.append(0)
        pA1_Set_A.append(match.setsGanhos['A'])
        pA1_Set_B.append(match.setsGanhos['B'])
        pA1_Games.append(match.totalGames)
        pA1_Rounds.append(match.totalRounds)
    file1_human_readable.close()
    file1_machine_readable = open('partida1_machine_readable.txt', 'w')
    sys.stdout = file1_machine_readable
    for i in range(0,n):
        print(f"{pA1_Vencedor[i]} {pA1_Set_A[i]} {pA1_Set_B[i]} {pA1_Games[i]} {pA1_Rounds[i]}")
    file1_machine_readable.close()
    # Abre arquivo da partida 2 e redireciona os prints
    file2_human_readable = open('partida2_human_readable.txt', 'w')
    sys.stdout = file2_human_readable

    # Partida 2: os jogadores possuem nível técnico equivalente
    for i in range(0, n):
        print(f"-- SIMULACAO {i+1}")

        match = Partida(pA2) 
        match.joga_partida()
        
        resultado(match)
        if match.vencedor == "A":
           pA2_Vencedor.append(1)
        else:
           pA2_Vencedor.append(0)
        
        pA2_Set_A.append(match.setsGanhos['A'])
        pA2_Set_B.append(match.setsGanhos['B'])
        pA2_Games.append(match.totalGames)
        pA2_Rounds.append(match.totalRounds)
    file2_human_readable.close()
    file2_machine_readable = open('partida2_machine_readable.txt', 'w')
    sys.stdout = file2_machine_readable
    for i in range(0,n):
        print(f"{pA2_Vencedor[i]} {pA2_Set_A[i]} {pA2_Set_B[i]} {pA2_Games[i]} {pA2_Rounds[i]}")
    file2_machine_readable.close()
    sys.stdout = orig_stdout
    pA1_dt = pd.read_csv('partida1_machine_readable.txt', sep=" ", header=None)
    pA1_dt.columns = ["Vencedor","Pontos Set A","Pontos Set B", "Games", "Rounds"]
    pA2_dt = pd.read_csv('partida2_machine_readable.txt', sep=" ", header=None)
    pA2_dt.columns = ["Vencedor","Pontos Set A","Pontos Set B", "Games", "Rounds"]


    print("Resultados de 3 jogos escolhidos aleatoriamente da partida 1")
    print(pA1_dt.sample(3).describe())
    print("Resultados de 3 jogos escolhidos aleatoriamente da partida 2")
    print(pA2_dt.sample(3).describe())

    pA1_partial_dt = pA1_dt.sample(10)
    pA2_partial_dt = pA2_dt.sample(10)
    
    print("Resultados de 10 jogos escolhidos aleatoriamente da partida 1")
    print(pA1_partial_dt.describe())
    print("Resultados de 10 jogos escolhidos aleatoriamente da partida 2")
    print(pA2_partial_dt.describe())
if __name__ == "__main__":
    main()