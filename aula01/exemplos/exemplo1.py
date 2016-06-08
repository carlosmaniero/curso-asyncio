import random


def lancar_dados(n):
    dados = []
    for i in range(0, n):
        dados.append(random.randint(1, 6))
    return dados
