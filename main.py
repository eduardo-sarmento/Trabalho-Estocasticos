from jogo import Partida

# 1 partida = melhor de 3 sets
# 1 set = melhor de 7 games
# 1 game = cadeia de markov

def main():
    j = Partida(0.5)
    j.joga_partida()

    print(j.vencedor)
    print(j.setsGanhos)

if __name__ == "__main__":
    main()