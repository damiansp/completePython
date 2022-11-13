import threading
import time


thread_lock = threading.Lock()


def main():
    thr1 = MyThread('A', 0.5)
    thr2 = MyThread('B', 0.6)
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    print('Finished.')
                

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Starting thread {self.name}')
        thread_lock.acquire()
        self._thread_countdown()
        thread_lock.release()
        print(f'Finished {self.name}')

    def _gthread_countdown(self):
        counter = 5
        while counter:
            time.sleep(self.delay)
            print(f'Thread {self.name} counting down: {counter}...')
            counter -= 1


if __name__ == '__main__':
    main()
