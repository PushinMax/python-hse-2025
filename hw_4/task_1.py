import time
from multiprocessing import Process
import threading

def fib(n: int):
    a = 1
    b = 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

def pross(n: int):
    start_time = time.time()
    l = []
    for i in range(10):
        l.append(Process(target=fib, args=(n,)))
        l[i].start()

    for i in range(10):
        l[i].join()
    end_time = time.time()
    print(f"Время выполнения через процессы: {end_time - start_time:.4f} секунд")

def thread(n: int):
    start_time = time.time()
    l = []
    for i in range(10):
        l.append(threading.Thread(target=fib, args=(n,)))
        l[i].start()

    for i in range(10):
        l[i].join()
    end_time = time.time()
    print(f"Время выполнения через треды: {end_time - start_time:.4f} секунд")

n = 10 ** 6
pross(n)
thread(n)