import csv
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
                yield from facto_n(x // n, n)
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
    return csv.reader(source, delimiter='\t')

with open('Anscombe.txt') as source:
    print(list(row_iter(source)))
