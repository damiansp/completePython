from threading import Thread
import time

import requests


SYMBOLS = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')
BASES = ('USD', 'EUR', 'PLN', 'NOK', 'CZK')


def fetch_rates(base):
    resp = requests.get(f'https://api.vatcomply.com/rates?base={base}')
    resp.raise_for_status()
    rates = resp.json()['rates']
    rates[base] = 1.
    rates_line = ', '.join([f'{rates[sym]:7.03} {sym}' for sym in SYMBOLS])
    print(f'1 {base}: {rates_line}')
    

def main():
    threads = []
    for base in BASES:
        thread = Thread(target=fetch_rates, args=[base])
        thread.start()
        threads.append(thread)
    while threads:
        threads.pop().join()


if __name__ == '__main__':
    start = time.time()
    main()
    elapsed = time.time() - start
    print(f'\ntime elapsed: {elapsed:.2f} s')
