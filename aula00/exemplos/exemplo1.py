import threading
import time

contador = 0
max_for = 10000000
paralelo = True

lock = threading.Lock()

def somar():
    global contador
    for i in range(0, max_for):
        lock.acquire()
        contador += 1
        lock.release()

start_time = time.time()
if paralelo:
    t1 = threading.Thread(target=somar)
    t2 = threading.Thread(target=somar)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
else:
    somar()
    somar()
end_time = time.time() - start_time

print(end_time)
print(contador)

# Tempo Serial
# 1.5447351932525635, 1.5824646949768066, 1.5824646949768066

# Tempo Paralelo
# 1.686720848083496, 1.568105697631836, 1.8095057010650635
