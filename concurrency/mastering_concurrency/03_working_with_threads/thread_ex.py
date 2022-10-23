import threading
import time


def main():
    t1 = MyThread('A', 0.5)
    t2 = MyThread('B', 0.6)
    t3 = MyThread('C', 0.8)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('And done.')

    
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Starting thread {self.name}')
        self._countdown()
        print(f'Finished thread {self.name}')

    def _countdown(self):
        counter = 5
        while counter:
            time.sleep(self.delay)
            print(f'  Thread {self.name} counting down: {counter}')
            counter -= 1


if __name__ == '__main__':
    main()
