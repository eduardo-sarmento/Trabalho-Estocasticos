from jogo import Jogo
def main():
    j = Jogo(0.5)
    vencedor,resultado = j.joga()
    print(vencedor)
    print(resultado)

if __name__ == "__main__":
    main()