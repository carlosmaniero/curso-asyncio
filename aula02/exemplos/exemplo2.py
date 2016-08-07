import queue
contador = 0
max_for = 10000000


def somar_1000(task_name):
    yield
    global contador
    print('Executing {}'.format(task_name))
    for i in range(0, 1000):
        contador += 1


def somar(task_name):
    global contador
    for i in range(0, max_for):
        print('Executing {}'.format(task_name))
        yield somar_1000('somar_1000_{}'.format(task_name))


q = queue.Queue()
q.put(somar('task_somar_1'))
q.put(somar('task_somar_2'))


while not q.empty():
    task = q.get()
    try:
        fn = next(task)
        if fn:
            q.put(fn)
    except StopIteration:
        pass
    else:
        q.put(task)

print(contador)
