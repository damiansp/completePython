import timeit


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def test_fib(benchmark):
    assert benchmark(fib, 30)
    

if __name__ == '__main__':
    print(timeit.timeit('fib(30)', setup='from __main__ import fib'))
