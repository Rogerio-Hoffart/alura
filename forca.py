import random

def jogar():

    mensagem_de_abertura()

    secret_word = carrega_palavra_secreta()

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
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do Jogo!")

def mensagem_de_abertura():
    print("********************************")
    print("**Bem vindo ao jogo de Forca!**")
    print("********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
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
    jogadas = 6
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
    return letras_certas, erros

if (__name__ == "__main__"):
    jogar()