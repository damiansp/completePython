from math import sqrt
import threading


def main():
    inputs = [2, 193, 323, 1327, 433_785_905, 433_785_907, 433_785_909]
    threads = []
    for x in inputs:
        thread = MyThread(x)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print('Dunzo!')
    

class MyThread(threading.Thread):
    def __init__(self, x):
        super().__init__()
        self.x = x

    def run(self):
        print(f'Starting is_prime({self.x})...\n')
        is_prime(self.x)


def is_prime(x):
    if x < 2:
        print(f'{x} is not prime')
        return
    if x == 2:
        print(f'{x} is prime')
        return
    if x % 2 == 0:
        print(f'{x} is not prime')
        return
    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            print(f'{x} is not prime')
            return
    print(f'{x} is prime')


if __name__ == '__main__':
    main()
