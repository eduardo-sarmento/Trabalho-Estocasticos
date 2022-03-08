from jogo import Partida
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
    pA1 = 0.75 # Probabilidade de A na partida 1
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
    file1 = open('partida1.txt', 'w')
    sys.stdout = file1

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

    # Abre arquivo da partida 2 e redireciona os prints
    file2 = open('partida2.txt', 'w')
    sys.stdout = file2

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
    pA1_dict = {"Vencedor" : pA1_Vencedor,"Set A" : pA1_Set_A,"Set B" : pA1_Set_B, "Games": pA1_Games, "Rounds" : pA1_Rounds}
    pA2_dict = {"Vencedor" : pA2_Vencedor,"Set A" : pA2_Set_A,"Set B" : pA2_Set_B, "Games": pA2_Games, "Rounds" : pA2_Rounds}
    pA1_dt = pd.DataFrame(pA1_dict)
    pA2_dt = pd.DataFrame(pA2_dict)

    file1.close()
    file2.close()
    sys.stdout = orig_stdout
    print(pA1_dt.describe())
    print(pA2_dt.describe())
if __name__ == "__main__":
    main()