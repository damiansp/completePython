from multiprocessing import Process
from time import sleep


def main():
    process = CustomProcess()
    process.start()
    print('Awaiting processes...')
    process.join()


class CustomProcess(Process):
    @staticmethod
    def run():
        sleep(1)
        print('Et voila, message from a custom process.')


if __name__ == '__main__':
    main()
