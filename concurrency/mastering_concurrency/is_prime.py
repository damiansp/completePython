from concurrent import futures
from concurrent.futures import ProcessPoolExecutor
from timeit import default_timer as timer
from math import sqrt


def main():
    data = [i for i in range(10 ** 13, 10 ** 13 + 500)]
    sequential(data)
    concurrent(data)


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return True


def sequential(data):
    print('Running sequentially...')
    start = timer()
    res = []
    for i in data:
        if is_prime(i):
            res.append(i)
    print('Results:', res)
    print(f'Time: {timer() - start:.2f} s')


def concurrent(data):
    print('Running concurrent...')
    start = timer()
    res = []
    with ProcessPoolExecutor(max_workers=20) as executor:
        futs = [executor.submit(is_prime, i) for i in data]
        for i, future in enumerate(futures.as_completed(futs)):
            if future.result():
                res.append(data[i])
    print('Results:', res)
    print(f'Time: {timer() - start:.2f} s')


if __name__ == '__main__':
    main()
