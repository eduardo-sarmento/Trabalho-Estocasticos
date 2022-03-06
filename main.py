from jogo import Partida
import sys

# 1 partida = melhor de 3 sets
# 1 set = melhor de 7 games
# 1 game = cadeia de markov

def resultado(match):
    print(f"======= Vencedor da partida: {match.vencedor}")
    print(f"======= Resultado da partida (A - B):  {match.setsGanhos['A']} - {match.setsGanhos['B']}")


def main():
    n = 30 # Numero de simulacoes por partida
    pA1 = 0.85 # Probabilidade de A na partida 1
    pA2 = 0.45 # Probabilidade de A na partida 2

    vitorias1_p1 = 0 # Vitórias de A na partida 1
    sets_p1 = 0 # Sets da partida 1
    V1sets_p1 = 0 # sets vencidos por A na partida 1

    vitorias1_p2 = 0 # Vitorias de A na partida 2
    sets_p2 = 0 # Sets da partida 2
    V1sets_p2 = 0 # sets vencidos por A na partida 2

    orig_stdout = sys.stdout

    # Abre arquivo da partida 1 e redireciona os prints
    file1 = open('partida1.txt', 'w')
    sys.stdout = file1

    # Partida 1: o Jogador A é muito melhor do que o Jogador B
    for i in range(n):
        print(f"-- SIMULACAO {i}")

        match = Partida(pA1) 
        match.joga_partida()

        if(match.vencedor == 'A'): vitorias1_p1+=1    
        sets_p1 += match.setsJogados
        V1sets_p1 += match.setsGanhos['A']
        
        resultado(match)
    print(f"\nVitorias A: {vitorias1_p1} :: Vitorias B: {n-vitorias1_p1}")
    print(f"Sets ganhos por A: {V1sets_p1} :: Sets ganhos B: {sets_p1-V1sets_p1}")

    # Abre arquivo da partida 2 e redireciona os prints
    file2 = open('partida2.txt', 'w')
    sys.stdout = file2

    # Partida 2: os jogadores possuem nível técnico equivalente
    for i in range(0, n):
        print(f"-- SIMULACAO {i}")

        match = Partida(pA2) 
        match.joga_partida()

        if(match.vencedor == 'A'): vitorias1_p2+=1 
        sets_p2 += match.setsJogados
        V1sets_p2 += match.setsGanhos['A']
        
        resultado(match)
    print(f"\nVitorias A: {vitorias1_p2} :: Vitorias B: {n-vitorias1_p2}")
    print(f"Sets ganhos por A: {V1sets_p2} :: Sets ganhos B: {sets_p2-V1sets_p2}")



    file1.close()
    file2.close()
    sys.stdout = orig_stdout


if __name__ == "__main__":
    main()