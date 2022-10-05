from multiprocessing import Process, RLock
from random import random
from time import sleep


def main():
    lock = RLock()
    procs = [Process(target=task, args=(lock, i, random())) for i in range(10)]
    for proc in procs:
        proc.start()
    print('Awaiting processes...')
    for proc in procs:
        proc.join()


def task(lock, identifier, value):
    with lock:
        print(f'> process {identifier} sleeping for {value:.3f}')
        sleep(value)
    print(f'  --{identifier} intermission--')
    report(lock, identifier)


def report(lock, identifier):
    with lock:
        print(f' >> process {identifier}: Mission accomplished')


if __name__ == '__main__':
    main()
