from multiprocessing import Condition, Process
from time import sleep


def main():
    cond = Condition()
    print('Main process waiting for data...')
    with cond:
        worker = Process(target=task, args=(cond,))
        worker.start()
        cond.wait()
    print('Main process complete')


def task(cond):
    sleep(1)
    print('Child process sending notification...', flush=True)
    with cond:
        cond.notify()
        # whatever...
    sleep(1)


if __name__ == '__main__':
    main()
