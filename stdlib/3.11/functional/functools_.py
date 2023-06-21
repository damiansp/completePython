from functools import cache, cached_property, lru_cache
import statistics
import urllib


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


print(factorial(10))  # 11 recursive calls
print(factorial(5))   # looks up cached value
print(factorial(12))  # 2 new recursive calls


class DataSet:
    def __init__(self, number_seq):
        self._data = tuple(number_seq)

    @cached_property
    def sd(self):
        return statistics.stdev(self._data)


@lru_cache  # default maxsize = 128
def count_vowels(sent):
    return sum(sent.lower().count(v) for v in 'aeiou')


@lru_cache(maxsize=32)
def get_pep(n):
    'Retrieve text of Python Enhancement Proposal'
    res = f'https://peps.python.org/pep-{n:04d}/'
    try:
        with urllib.request.urlopen(res) as pep:
            return pep.read()
    except urllib.error.HTTPError:
        return 'not found'


@lru_cache(maxsize=None)
def fib(n):
    return (n if n < 2 else fib(n - 1) + fib(n - 2))
        
