import random


class LancarDados(object):
    def __init__(self, n):
        self.n = n
        self.cursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < self.n:
            self.cursor += 1
            return random.randint(1, 6)
        else:
            raise StopIteration


for dado in LancarDados(10):
    print(dado)
