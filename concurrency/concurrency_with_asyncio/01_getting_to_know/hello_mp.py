import multiprocessing as mp
import os


def main():
    hello_proc = mp.Process(target=hello_from_process)
    hello_proc.start()
    print(f'Hello from main process ({os.getpid()})!')
    hello_proc.join()


def hello_from_process():
    print(f'Hello from child process ({os.getpid()})!')


if __name__ == '__main__':
    main()
