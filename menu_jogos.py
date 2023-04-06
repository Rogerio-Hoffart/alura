import advinha
import forca

def menu():
    print("********************************")
    print("*******Escolha o seu Jogo!******")
    print("********************************")

    print("(1) Forca (2) Advinhação:")

    jogo = int(input("Qual Jogo? - "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        advinha.jogar()

if (__name__ == "__main__"):
    menu()