import functools
import timeit


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def list_factorials(n):
    return [factorial(i) for i in range(n + 1)]


print(list_factorials(10))


setup = 'from __main__ import list_factorials'
statement = 'list_factorials(60)'
dur = timeit.timeit(statement, setup=setup, number=1000)
print(f'No caching; duration: {dur}')


cache = {}


def fact(n):
    if n not in cache:
        if n == 1:
            cache[n] = 1
        else:
            cache[n] = n * fact(n - 1)
    return cache[n]


def list_facts(n):
    global cache
    cache = {}
    return [fact(i) for i in range(1, n + 1)]

print(list_facts(10))


setup = 'from __main__ import list_facts; cache = {}'
statement = 'list_facts(60)'
dur = timeit.timeit(statement, setup=setup, number=1000)
print(f'Manual caching; duration: {dur}')


@functools.lru_cache()
def factc(n):
    if n == 1:
        return 1
    return n * factc(n - 1)


def list_factc(n):
    return [factc(i) for i in range(1, n + 1)]


setup = 'from __main__ import list_factc'
statement = 'list_factc(60)'
dur = timeit.timeit(statement, setup=setup, number=1000)
print(f'LRU caching; duration: {dur}')

