from multiprocessing import Barrier, Process
from random import random
from time import sleep


def main():
    N_PROCS = 10
    barrier = Barrier(N_PROCS + 1)
    for i in range(N_PROCS):
        worker = Process(target=task, args=(barrier, i))
        worker.start()
    print('Main waiting on all results')
    barrier.wait()
    print('All processes in batch have results.')


def task(barrier, n):
    val = 10 * random()
    sleep(val)
    print(f'Process {n} done; got {val}')
    barrier.wait()  # waitfor all other barred processes to complete


if __name__ == '__main__':
    main()
    
