import threading
import time


def print_fib(nmbr: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        if n ==2:
            return 1
        return fib(n - 1) + fib(n - 2)
    print(f'fib({nmbr}): {fib(nmbr)}')


def fibs_threaded():
    thread_35 = threading.Thread(target=print_fib, args=(35,))
    thread_36 = threading.Thread(target=print_fib, args=(36,))
    thread_35.start()
    thread_36.start()
    thread_35.join()
    thread_36.join()


if __name__ == '__main__':
    start = time.time()
    fibs_threaded()
    end = time.time()
    print(f'Elapsed: {end - start:.4f}s')
    
