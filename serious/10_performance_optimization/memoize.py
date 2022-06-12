import functools
import math


_SIN_MEMOIZED_VALS = {}


def memoized_sin(x):
    if x not in _SIN_MEMOIZED_VALS:
        _SIN_MEMOIZED_VALS[x] = math.sin(x)
    return _SIN_MEMOIZED_VALS[x]

print(memoized_sin(1))
print(memoized_sin(2))
print(_SIN_MEMOIZED_VALS)


@functools.lru_cache(maxsize=2)
def mem_sin(x):
    return math.sin(x)

print(mem_sin(2))
print(mem_sin.cache_info())
mem_sin.cache_clear()
print(mem_sin.cache_info())
