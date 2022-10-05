from multiprocessing import Process, Semaphore
from random import random
from time import sleep


def main():
    semaphore = Semaphore(2)
    procs = [Process(target=task, args=(semaphore, i)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()


def task(semaphore, n):
    with semaphore:
        value = random()
        sleep(value)
        print(f'Process {n} got {value}')


if __name__ == '__main__':
    main()
