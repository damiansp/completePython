import csv
from   collections import namedtuple
import itertools
import math


# Generator expressions
def pfactorsl(x):
    if x % 2 == 0:
        yield 2
        if x // 2 > 1: 
            yield from pfactorsl(x // 2)
        return
    for i in range(3, int(math.sqrt(x) + 0.5) + 1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from pfactorsl(x // i)
            return
    yield x


def pfactorsr(x):
    def factor_n(x, n):
        if n * n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x // n, n)
        else:
            yield from factor_n(x, n + 2)
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactorsr(x // 2)
        return
    yield from factor_n(x, 3)


print(pfactorsl(1560))
print(list(pfactorsl(1560)))
                
                                   
def limits(iterable):
    max_tee, min_tee = itertools.tee(iterable, 2)
    return max(max_tee), min(min_tee)


# Combining generator expressions
# g_f_x = (g(f(x)) for x in range(...))
# g_f_x = (g(y) for y in (f(x) for x in range(...)))

def row_iter(source):
    return csv.reader(source, delimiter=',')

with open('Anscombe.txt') as source:
    print(list(row_iter(source)))


def head_split_fixed(row_iter):
    title = next(row_iter)
    assert len(title) == 1 and title[0] == 'Anscombe\'s quartet'
    heading = next(row_iter)
    print(heading)
    assert len(heading) == 4 and heading == ['I', 'II', 'III', 'IV']
    columns = next(row_iter)
    assert len(columns) == 8 and columns == ['x', 'y'] * 4
    return row_iter

with open('Anscombe.txt')as source:
    print(list(head_split_fixed(row_iter(source))))


# Lists, dicts, sets
Pair = namedtuple('Pair', ('x', 'y'))


def series(n, row_iter):
    for row in row_iter:
        yield Pair(*row[n * 2:n * 2 + 2])


with open('Anscombe.txt') as source:
    data = tuple(head_split_fixed(row_iter(source)))
    s1 = tuple(series(0, data))
    s2 = tuple(series(1, data))
    s3 = tuple(series(2, data))
    s4 = tuple(series(3, data))

print(s4)
