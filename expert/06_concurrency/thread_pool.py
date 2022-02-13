from queue import Empty, Queue
from threading import Thread
import time

import requests


THREAD_POOL_SIZE = 4
SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')


def main():
    q = Queue()
    for base in BASES:
        q.put(base)
    threads = [Thread(target=worker, args=(q,))
               for _ in range(THREAD_POOL_SIZE)]
    for thread in threads:
        thread.start()
    q.join()
    while threads:
        threads.pop().join()


def worker(q):
    while not q.empty():
        try:
            item = q.get_nowait()
        except Empty:
            break
        else:
            fetch_rates(item)
            q.task_done()


def fetch_rates(base):
    resp = requests.get(f'https://api.vatcomply.com/rates?base={base}')
    resp.raise_for_status()
    rates = resp.json()['rates']
    rates[base] = 1.
    rates_line = ', '.join([f'{rates[sym]:7.03} {sym}' for sym in SYMBOLS])
    print(f'1 {base}: {rates_line}')
    

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f'\ntime elapsed: {elapsed:.2f} s')
