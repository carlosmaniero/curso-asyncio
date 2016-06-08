import random


def lancar_dados(n):
    print('Função iniciada')
    for i in range(0, n):
        print('entrou no for')
        yield random.randint(1, 6)
        print('saiu do for')
    print('fim da função')
