# __author__ = Diego Denzer


def f1():
    palavras = []
    frase = ['abelha']
    with open('palavras.txt') as arquivo:
        for linha in arquivo:
            print(linha)
            palavras.append(linha)
    print(palavras)
    result = [0 for i in palavras]

    for p in frase:
        print(p)
        i = palavras.index(p)
        palavras[i] = 1

f1()