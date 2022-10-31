import time


def print_fib(nmbr: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    print(f'fib({nmbr}): {fib(nmbr)}')


def fibs_no_threading():
    print_fib(35)
    print_fib(36)


if __name__ == '__main__':
    start = time.time()
    fibs_no_threading()
    end = time.time()
    print(f'Elapsed: {end - start:.4f}s')
