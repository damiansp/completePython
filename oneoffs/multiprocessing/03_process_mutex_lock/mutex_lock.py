from multiprocessing import Lock, Process
from random import random
from time import sleep


def main():
    lock = Lock()
    processes = [
        Process(target=task, args=(lock, i, random())) for i in range(10)]
    for process in processes:
        process.start()
    print('Awaiting processes...')
    for process in processes:
        process.join()
        


def task(lock, identifier, value):
    with lock:
        print(f'> process {identifier} has lock for {value} s')
        sleep(value)


if __name__ == '__main__':
    main()
