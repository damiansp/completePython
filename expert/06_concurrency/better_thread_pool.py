from queue import Empty, Queue
from threading import Thread
import time

import requests


THREAD_POOL_SIZE = 4
SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')


def main():
    work_q = Queue()
    results_q = Queue()
    for base in BASES:
        work_q.put(base)
    threads = [Thread(target=worker, args=(work_q, results_q))
               for _ in range(THREAD_POOL_SIZE)]
    for thread in threads:
        thread.start()
    work_q.join()
    while threads:
        threads.pop().join()
    while not results_q.empty():
        present_result(*results_q.get())


def worker(work_q, results_q):
    while not work_q.empty():
        try:
            item = work_q.get_nowait()
        except Empty:
            break
        else:
            results_q.put(fetch_rates(item))
            work_q.task_done()
            

def fetch_rates(base):
    resp = requests.get(f'https://api.vatcomply.com/rates?base={base}')
    resp.raise_for_status()
    rates = resp.json()['rates']
    rates[base] = 1.
    return base, rates


def present_result(base, rates):
    rates_line = ', '.join([f'{rates[sym]:7.03} {sym}' for sym in SYMBOLS])
    print(f'1 {base}: {rates_line}')
    

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f'\ntime elapsed: {elapsed:.2f} s')
