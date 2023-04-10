import random

def jogar():

    mensagem_de_abertura()

    secret_word = carrega_palavra_secreta("nomes.txt")

    enforcou, acertou, letras_certas, erros, jogadas = inicializacao_var(secret_word)

    while( not enforcou and not acertou ):
        chute = chuta_letra()
        index = 0
        acerto = False
        letras_certas, erros = testa_chute(secret_word, index, acerto, chute, letras_certas, erros, jogadas)
        print(letras_certas)
        letras_faltando = str(letras_certas.count("_"))
        print("Ainda faltam acertar {} letras".format(letras_faltando))
        if (jogadas == erros):
            enforcou = True
        acertou = "_" not in letras_certas

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(secret_word)

def mensagem_de_abertura():
    print("********************************")
    print("**Bem vindo ao jogo de Forca!**")
    print("********************************")

def carrega_palavra_secreta(nome_arquivo = "palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    secret_word = palavras[random.randrange(0, len(palavras))]
    return secret_word
def inicializacao_var(palavra):
    enforcou = False
    acertou = False
    erros = 0
    jogadas = 7
    letras_certas = ["_" for x in palavra]
    print(letras_certas)
    print("Você tem {} tentativas.".format(jogadas))
    return enforcou, acertou, letras_certas, erros, jogadas

def chuta_letra():
    chute = input("Qual letra?")
    chute = chute.strip()
    return chute

def testa_chute(secret_word, index, acerto, chute, letras_certas, erros, jogadas):
    for letra in secret_word.upper():
        if chute.upper() == letra:
            letras_certas[index] = letra
            acerto = True
        index += 1
        if (index == len(secret_word) and acerto == False):
            erros += 1
            print("Você errou, ainda possui {} tentativas.".format(jogadas - erros))
            desenha_forca(erros)
    return letras_certas, erros

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()