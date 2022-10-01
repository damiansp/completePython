from multiprocessing import Process
from time import sleep


def main():
    process = Process(target=task, args=(1.5, 'What up, yo?'))
    process.start()
    print('Awaiting processes...')
    process.join()


def task(sleep_time, msg):
    sleep(sleep_time)
    print(msg)


if __name__ == '__main__':
    main()
