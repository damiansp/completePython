from collections.abc import Mapping
from decimal import Decimal
from functools import (
    cache, cached_property, lru_cache, partial, partialmethod, singledispatch,
    singledispatchmethod, total_ordering, wraps)
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
        

# Given a def of == and at least one of <, <=, >, >=, <total_ordering> can
# figure out the remaining comparisons
@total_ordering
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def _is_valid_operand(self, other):
        # compared obj does not have to be Student, but must have name and
        # surname
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


# partial(f, *args, **kwargs) like:
# f(*args, **kwargs)
base_two = partial(int, base=2)
base_two.__doc__ = 'Convert base-two string to (base 10) int'
print(base_two('10101'))  # 21


class Cell:
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)  # False
c.set_alive()
print(c.alive)  # True


@singledispatch
def f(arg, verbose=False):
    if verbose:
        print('Please allow me to say', end=' ')
    print(arg)


@f.register
def _(arg: list, verbose=False):
    if verbose:
        print('Enumerate this:')
    for i, elem in enumerate(arg):
        print(i, elem)


# could also do:
# from typing import Union
# ...(arg: Union[int, float], ...)
@f.register
def _(arg: int | float, verbose=False):
    if verbose:
        print('Strength in numbers eh, with', end=' ')
    print(arg)


@f.register(complex)
def _(arg, verbose=False):
    if verbose:
        print('Better than complicated.', end=' ')
    print(f'{arg.real}+{arg.imag}i')


def nothing(arg, verbose=False):
    print('Nothing!')


f.register(type(None), nothing)


@f.register(float)
@f.register(Decimal)
def f_num(arg, verbose=False):
    if verbose:
        print('Half of your number:', end=' ')
    print(arg / 2)


@f.register
def _(arg: Mapping, verbose=False):
    if verbose:
        print('Keys AND values!')
    for k, v in arg.items():
        print(k, ' => ', v)


print(f_num is f)  # False

f('Hello, World!')
f('test.', verbose=True)
f(42, verbose=True)
f(['ham', 'ham', 'eggs', 'spam'], verbose=True)
f(None)
f(1.234)

print(f.dispatch(float))
print(f.dispatch(dict))
print(f.registry.keys())
print(f.registry[float])
print(f.registry[object])


class Negator:
    @singledispatchmethod
    def neg(self, arg):
        raise NotImplementedError(f'Cannot negate a {type(arg)}')

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _(self, arg: bool):
        return not arg


class Negator2:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError(f'Cannot negate a {type(arg)}')

    @neg.register
    @classmethod
    def _(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def _(cls, arg: bool):
        return not arg

    
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Called decorated function')
        return f(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    'Example docstring'
    print('Called example()')


example()
# properly wrapped:
print(example.__name__)
print(example.__doc__)
