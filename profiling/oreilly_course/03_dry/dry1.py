from math import sin
import timeit

import numpy as np


def sum_of_squares1():
    total = 0
    for x in range(100):
        for y in range(100):
            xsq = x ** 2
            ysq = y ** 2
            total += xsq + ysq
    return total


def sum_of_squares2():
    total = 0
    for x in range(100):
        xsq = x ** 2 ### <-
        for y in range(100):
            ysq = y ** 2
            total += xsq + ysq
    return total


def sum_of_squares3():
    total = 0
    for x in range(100):
        total += (100 * x**2)
        for y in range(100):
            total += y ** 2
    return total


for func in sum_of_squares1, sum_of_squares2, sum_of_squares3:
    name = func.__name__
    setup = f'from __main__ import {name}'
    dur = timeit.timeit(f'{name}()', setup=setup, number=100)
    print(f'{name}, res: {func()}, duration: {dur}')


def sin_sum1():
    tot = 0
    for x in range(10_000):
        tot += sin(x)
    return tot


def sin_sum2():
    tot = 0
    local_sin = sin
    for x in range(10_000):
        tot += local_sin(x)
    return tot


for func in sin_sum1, sin_sum2:
    name = func.__name__
    setup = f'from __main__ import {name}'
    dur = timeit.timeit(f'{name}()', setup=setup, number=100)
    print(f'{name}, res: {func()}, duration: {dur}')
