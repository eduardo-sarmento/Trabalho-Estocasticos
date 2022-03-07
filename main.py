from jogo import Partida
import sys

# 1 partida = melhor de 3 sets
# 1 set = melhor de 7 games
# 1 game = cadeia de markov

def resultado(match):
    print(f"======= Vencedor da partida: {match.vencedor}")
    print(f"======= Resultado da partida (A - B):  {match.setsGanhos['A']} - {match.setsGanhos['B']}")
    print(f"======= Todal de Games jogados na partida: {match.totalGames}")
    print(f"======= Todal de Rounds jogados na partida: {match.totalRounds}")


def main():
    n = 2 # Numero de simulacoes por partida
    pA1 = 0.85 # Probabilidade de A na partida 1
    pA2 = 0.45 # Probabilidade de A na partida 2

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

    # Abre arquivo da partida 2 e redireciona os prints
    file2 = open('partida2.txt', 'w')
    sys.stdout = file2

    # Partida 2: os jogadores possuem nível técnico equivalente
    for i in range(0, n):
        print(f"-- SIMULACAO {i+1}")

        match = Partida(pA2) 
        match.joga_partida()
        
        resultado(match)

    file1.close()
    file2.close()
    sys.stdout = orig_stdout


if __name__ == "__main__":
    main()