import requests
import threading
import time


def read_example() -> None:
    resp = requests.get('https://www.example.com')
    print(resp.status_code)


if __name__ == '__main__':
    start = time.time()
    thr1 = threading.Thread(target=read_example)
    thr2 = threading.Thread(target=read_example)
    thr1.start()
    thr2.start()
    print('All threads running')
    thr1.join()
    thr2.join()
    end = time.time()
    print(f'Elapsed: {end - start:.4f}s')
