from functools import cache, cached_property, lru_cache, total_ordering
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
        

# Given a def of == and at least one of <, <=, >, >=, <total_ordering> can figure out
# the remaining comparisons
@total_ordering
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def _is_valid_operand(self, other):
        # compared obj does not have to be Student, but must have name and surname
        return (hasattr(other, 'name') and hasattr(other, 'surname'))

    def __eq__(self, other):
        if self._is_valid_operand(other):
            return (
                (self.surname.lower(), self.name.lower())
                == (other.surname.lower(), other.name.lower()))
        return NotImplemented

    def __lt__(self, other):
        if self._is_valid_operand(other):
            return (
                (self.lastname.lower(), self.name.lower())
                < (other.surname.lower(), other.name.lower()))
        return NotImplemented
