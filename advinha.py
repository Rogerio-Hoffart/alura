import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    secret_number = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Selecione o nível de dificuldade.")
    print("(1) Fácil, (2) Médio, (3) Difícil:")
    nivel = int(input("Define o nível:"))

    if (nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    while(tentativas > 0):
        print("Você tem {} tentativas".format(tentativas))
        user_try = input("Digite um número entre 1 e 100: ")
        user_number = int(user_try)

        if(user_number < 1 or user_number > 100):
            print("Digite um número entre 1 e 100!")
            continue

        print("Você Digitou: ", user_try)

        acerto = secret_number == user_number
        maior  = secret_number > user_number
        menor  = secret_number < user_number

        if (acerto):
            print("Voçê acertou e fez {} pontos!".format(pontos))
            tentativas = 0
        else:
            if (maior):
                print("O número secreto é maior!")
            elif (menor):
                print("O número secreto é menor!")
            print("Você errou!")
            pontos_perdidos = abs(secret_number - user_number)
            pontos = pontos - pontos_perdidos
        tentativas = tentativas - 1

    print("Fim de Jogo! O Número secreto era: {}".format(secret_number))

if (__name__ == "__main__"):
    jogar()