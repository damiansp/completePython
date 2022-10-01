from multiprocessing import Process, Value
from time import sleep


def main():
    process = CustomProcess()
    process.start()
    print('Awaiting processes...')
    process.join()
    print(f'Parent got {process.data.value}')


class CustomProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.data = Value('i', 0)

    def run(self):
        sleep(1)
        self.data.value = 99
        print(f'Child stored: {self.data.value}')


if __name__ == '__main__':
    main()
