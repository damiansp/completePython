import queue as q
import threading
import time


my_q = q.Queue()


def main():
    inputs = [1, 10, 4, 3]
    for x in inputs:
        my_q.put(x)
    thr1 = MyThread('A')
    thr2 = MyThread('B')
    thr3 = MyThread('C')
    thr1.start()
    thr2.start()
    thr3.start()
    thr1.join()
    thr2.join()
    thr3.join()
    print('Done')


class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'Starting {self.name}.')
        self._process_queue()
        print(f'Exiting {self.name}')

    def _process_queue(self):
        while True:
            try:
                print('Checking the queue...')
                x = my_q.get(block=False)
            except q.Empty:
                print('Queue is empty')
                return
            else:
                self._print_factors(x)
            time.sleep(1)

    @staticmethod
    def _print_factors(x):
        res = f'Postive factors of {x} are:'
        for i in range(1, x + 1):
            if x % i == 0:
                res += f'{i} '
        res += '\n' + '_'*20
        print(res)


if __name__ == '__main__':
    main()
