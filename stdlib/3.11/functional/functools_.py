from functools import cache, cached_property
import statistics


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
