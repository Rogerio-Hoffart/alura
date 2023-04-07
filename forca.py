import random

def jogar():
    print("********************************")
    print("**Bem vindo ao jogo de Forca!**")
    print("********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    secret_word = palavras[random.randrange(0,len(palavras))]
    enforcou = False
    acertou = False
    erros = 0
    jogadas = 6
    letras_certas = ["_" for x in secret_word]
    print(letras_certas)
    print("Você tem {} tentativas.".format(jogadas))

    while( not enforcou and not acertou ):
        chute = input("Qual letra?")
        chute = chute.strip()
        index = 0
        acerto = False
        for letra in secret_word.upper():
            if chute.upper() == letra:
                letras_certas[index] = letra
                acerto = True
            index += 1
            if (index == len(secret_word) and acerto == False):
                erros += 1
                print("Você errou, ainda possui {} tentativas.".format(jogadas - erros))
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

if (__name__ == "__main__"):
    jogar()
