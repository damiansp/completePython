import multiprocessing as mp
from time import sleep


def task():
    sleep(1)
    print('This is from a process')


def main():
    process = mp.Process(target=task)
    process.start()
    print('Waiting for the process...')
    process.join()


if __name__ == '__main__':
    main()
