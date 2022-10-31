import requests
import time


def read_example() -> None:
    resp = requests.get('https://www.example.com')
    print(resp.status_code)


if __name__ == '__main__':
    start = time.time()
    read_example()
    read_example()
    end = time.time()
    print(f'Elapsed: {end - start:.4f}s')
