# Definicao dos estados da cadeia de markov
# O caminhamento no grafo é dado de acordo com https://miro.medium.com/max/700/1*O6gRCdf5W1Z_j0u_cQvbEw.png
# S0 => (0 - 0)
# S1 => (15 - Love)
# S2 => (30 - Love)
# S3 => (40 - Love)
# S4 => (Love - 15)
# S5 => (Love - 30)
# S6 => (Love - 40)
# S7 => (15 - 15)
# S8 => (30 - 15)
# S9 => (40 - 15)
# S10 => (15 - 30)
# S11 => (15 - 40)
# S12 => (Deuce)
# S13 => (Adv. A)
# S14 => (Adv. B)
# SWA => (A wins)
# SWB => (B wins)

def printS0():    print(f"0 - 0")
def printS1():    print(f"15 - Love")
def printS2():    print(f"30 - Love")
def printS3():    print(f"40 - Love")
def printS4():    print(f"Love - 15")
def printS5():    print(f"Love - 30")
def printS6():    print(f"Love - 40")
def printS7():    print(f"15 - 15")
def printS8():    print(f"30 - 15")
def printS9():    print(f"40 - 15")
def printS10():    print(f"15 - 30")
def printS11():    print(f"15 - 40")
def printS12():    print(f"Deuce")
def printS13():    print(f"Adv. A")
def printS14():    print(f"Adv. B")
def printSWA():    print(f"A wins")
def printSWB():    print(f"B wins")

# Faz o caminhamento no grafo de acordo com a direcao escolhida
def markovWalk(currentState, diretion):
    if diretion == 0:
        return markovWalkLeft(currentState)
    elif diretion == 1:
        return markovWalkRight(currentState)

# Segue para o prox estado tomando o caminho da ESQUERDA
def markovWalkLeft(currentState):
    nextState = None

    if currentState == "S0":
        printS0() # printa o estado inicial antes de caminhar na cadeia
        nextState = "S1"        
        printS1()
    elif currentState == "S1":
        nextState = "S2"  
        printS2()
    elif currentState == "S2":
        nextState = "S3"
        printS3()
    elif currentState == "S4":
        nextState = "S7"
        printS7()
    elif currentState == "S5":
        nextState = "S10"
        printS10()
    elif currentState == "S6":
        nextState = "S11"
        printS11()
    elif currentState == "S7":
        nextState = "S8"
        printS8()
    elif currentState == "S8":
        nextState = "S9"
        printS9()
    elif currentState == "S10":
        nextState = "S12"
        printS12()
    elif currentState == "S11":
        nextState = "S14"
        printS14()
    elif currentState == "S12":
        nextState = "S13"
        printS13()
    elif currentState == "S14":
        nextState = "S12"
        printS12()
    elif currentState == "S3" or currentState == "S9" or currentState == "S13":
        nextState = "SWA"
        printSWA()

    return nextState



# Segue para o prox estado tomando o caminho da DIREITA
def markovWalkRight(currentState):
    nextState = None

    if currentState == "S0":
        printS0() # printa o estado inicial antes de caminhar na cadeia
        nextState = "S4"        
        printS4()
    elif currentState == "S1":
        nextState = "S7"  
        printS7()
    elif currentState == "S2":
        nextState = "S8"
        printS8()
    elif currentState == "S3":
        nextState = "S9"
        printS9()
    elif currentState == "S4":
        nextState = "S5"
        printS5()
    elif currentState == "S5":
        nextState = "S6"
        printS6()
    elif currentState == "S7":
        nextState = "S10"
        printS10()
    elif currentState == "S8":
        nextState = "S12"
        printS12()
    elif currentState == "S9":
        nextState = "S13"
        printS13()
    elif currentState == "S10":
        nextState = "S11"
        printS11()
    elif currentState == "S12":
        nextState = "S14"
        printS14()
    elif currentState == "S13":
        nextState = "S12"
        printS12()
    elif currentState == "S6" or currentState == "S11" or currentState == "S14":
        nextState = "SWB"
        printSWB()

    return nextState