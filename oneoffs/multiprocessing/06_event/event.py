from multiprocessing import Event, Process
from random import random
from time import sleep


def main():
    event = Event()
    procs = [Process(target=task , args=(event, i)) for i in range(5)]
    for p in procs:
        p.start()
    print('Main process blocking...')
    sleep(2)
    event.set()  # triggers all child processes
    for p in procs:
        p.join()


def task(event, n):
    print(f'Process {n} waiting...', flush=True)
    event.wait()
    val = random()
    sleep(val)
    print(f'Process {n} got {val}.', flush=True)
             

if __name__ == '__main__':
    main()
