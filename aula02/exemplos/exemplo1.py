contador = 0
max_for = 10000000


def somar():
    global contador
    for i in range(0, max_for):
        contador += 1


somar()
somar()

print(contador)
