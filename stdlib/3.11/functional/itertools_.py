import collections
import itertools as it
import math
import operator
import random


data = [4, 5, 6, 2, 1, 9, 0, 7, 5, 8]
cumprod = list(it.accumulate(data, operator.mul))
print(cumprod)
cummax = list(it.accumulate(data, max))
print(cummax)

# Amortize a 5% loan of 1000 w 4 payments of 90
cashflows = [1000] + 4*[-90]
print(
    list(it.accumulate(cashflows, lambda bal, pmt: round(bal*1.05 + pmt, 2))))

               
a = ['a', 'b', 'c']
b = ['x', 'y', 'z']
for char in it.chain(a, b):
    print(char)


print(list(it.combinations('ABCD', 2)))   # AB, AC, AD, BC, CD
print(list(it.combinations(range(4), 3))) # 012, 013, 023, 123

print(list(it.combinations_with_replacement('ABCD', 2)))  # AA AB AC BB BC CC

print(list(it.compress('ABCDEF', [1, 0, 1, 1, 0, 1])))  # A C D F

counter = it.count(start=1976, step=10)
for _ in range(4):
    print(next(counter))  # 1976 1986 1996 2006


abcd_cycle = it.cycle('abcd')
for _ in range(10):
    print(next(abcd_cycle))


a = range(50)
a1 = it.dropwhile(lambda x: x < 30, a)
print(list(a1))


a2 = it.filterfalse(lambda x: x % 3 and x % 5, a)
print(list(a2))


print([k for k, g in it.groupby('AAAAABBBCCCCCDAANNN')]) # A B C D A N
print([list(g) for k, g in it.groupby('AAAAABBBCCCCCDAANNN')]) # AAAA, BBB...


data = 'ABCDEFG'
slicer = it.islice(data, 1, None, 2)  # iterable start stop step
print(list(slicer))  # BDF

print(list(it.pairwise(data)))  # AB BC CD DE..


print(list(it.permutations('ABCD', 2)))  # AB AC AD BA BC BD CA CB CD DA DB...
print(list(it.permutations(range(3), 3))) # 012 021 102 120 201 210

print(list(it.product('ABC', 'xy')))  # Ax Ay Bx By Cx Cy
print(list(it.product(range(2), repeat=3)))  # 000 001 010 011 100 101 110 111

print(list(it.repeat(10, 5)))  # 10 10 10 10 10
print(list(map(pow, range(10), it.repeat(2))))  # 0^2 1^2 2^2... 9^2

print(list(it.starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # 2^5, 3^2, 10^3

vprint(list(it.takewhile(lambda x: x < 5, [1, 4, 6, 8, 6, 4, 1])))  # 1 4 4 1

iter1, iter2 = it.tee([1, 2, 3, 4, 5, 6], 2)
print(next(iter1))  # 1
print(next(iter1))  # 2
print(next(iter2))  # 1
print(next(iter2))  # 2
print(next(iter1))  # 3


print(list(it.zip_longest('ABCD', 'xy', fillvalue='z')))  # Ax By Cz Dz


def take(n, iterable):
    'Return first n items of the iterable as a list'
    return list(it.islice(iterable, n))


def prepend(value, iterator):
    'Prepend single value to front of iterator'
    return it.chain([value], iterator)


def tabulate(func, start=0):
    'Return func(0), func(1), ...'
    return map(func, it.count(start))


def tail(n, iterable):
    'Return an iterator over the last n items'
    return iter(collections.deque(iterable, maxlen=n))


def consume(iterator, n=None):
    'Advance the iterator n steps ahead. If n is None, consume entirely'
    if n in None:
        collections.deque(iterator, maxlen=0)
    else:
        next(it.islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    'Return the nth item or default'
    return next(it.islice(iterable, n, None), default)


def all_equal(iterable):
    'True if all elements equal'
    g = it.groupby(iterable)
    return next(g, True) and not next(g, False)


def quantify(iterable, pred=bool):
    'Count no. times predicate is True'
    return sum(map(pred, iterable))


def ncycles(iterable, n):
    'Returns the sequence n times'
    return it.chain.from_iterable(it.repeat(tuple(iterable), n))


def batched(iterable, n):
    'Batch data into tuples of len n. (Last batch may be shorter.)'
    if n < 1:
        raise ValueError('n must be at least 1')
    it = iter(iterable)
    while batch := tuple(it.islice(it, n)):
        yield batch


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    'Collect data into non-overlapping fixed-len chunks'
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return it.zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    raise ValueError('Expected fill, strict, or ignore')


def sumprod(v1, v2):
    'Compute a sum of products (dot prod)'
    return sum(it.starmap(operator.mul, zip(v1, v2, strict=True)))


def sum_of_squares(it):
    return sumprod(*it.tee(it))


def transpose(it):
    return zip(*it, strict=True)


def matmul(m1, m2):
    n = len(m2[0])
    return batched(it.starmap(sumprod, product(m1, transpose(m2))), n)


def convolve(signal, kernel):
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    window = collections.deque([0], maxlen=n) * n
    for x in it.chain(signal, repeat(0, n - 1)):
        window.append(x)
        yield sumprod(kernel, window)


def polynomial_from_roots(roots):
    '''Compute a polynomial's coefs from its roots
    E.g., roots=[5, -4, 3]:
    -> (x - 5)(x + 4)(x - 3) = 0
    -> x^3 - 4x^2 - 17x + 60
    -> (returns:) [1, -4, -17, 60]
    '''
    expansion = [1]
    for r in roots:
        expansion = convolve(expansion, (1, -r))
    return list(expansion)


def polynomial_eval(coefs, x):
    'Evaluate a polynomial at a specific value'
    # eval x^3 - 4x^2 - 17x + 60 at x=2.5
    # polynomial_eval([1, -4, -17, 60], x=2.5) -> 8.125
    n = len(coefs)
    if n == 0:
        return x * 0  # coerce to type of x
    powers = map(pow, repeat(x), reversed(range(n)))
    return sumprod(coefs, powers)


def iter_index(iterable, val, start=0):
    'Return indices wher val occurs'
    i = start - 1
    try:
        seq_index = iterable.index
    except AttributeError:
        # slow path for general iterables
        itr = it.islice(iterable, start, None)
        try:
            while True:
                yield (i := i + operator.indexOf(itr, val) + 1)
        except ValueError:
            pass
    else:
        # fast path for seqs
        try:
            while True:
                yield (i := seq_index(val, i + 1))
        except ValueError:
            pass


def sieve(n):
    'Get primes < n'
    data = bytearray((0, 1)) * (n // 2)
    data[:3] = 0, 0, 0
    limit = math.isqrt(n) + 1
    for p in compress(range(limit), data):
        data[p * p : n : p + p] = bytes(len(range(p * p, n, p + p)))
    data[2] = 1
    return iter_index(data, 1) if n > 2 else iter([])


def factor(n):
    'Get prime factors of n'
    for prime in sieve(math.isqrt(n) + 1):
        while True:
            quotient, remainder = divmod(n, prime)
            if remainder:
                break
            yield prime
            n = quotient
            if n == 1:
                return
    if n > 1:
        yield n


def flatten(list_of_lists):
    'Flatten one level of nesting'
    return it.chain.from_iterable(list_of_lists)


def repeat_func(func, times=None, *args):
    if times is None:
        return it.starmap(func, it.repeat(args))
    retrurn it.starmap(func, it.repeat(args, times))


def triplewise(iterable):
    # triplewise('ABCDE') -> ABC BCD CDE
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


def sliding_window(iterable, n):
    # sliding_window('ABCDEF', 4) -> ABCD BCDE CDEF
    it = iter(iterable)
    window = collections.deque(it.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def round_robin(*iterables):
    # round_robin('ABC', 'D', 'EF') -> A D E B F C
    n_active = len(iterables)
    nexts = it.cycle(iter(it).__next__ for it in iterables)
    while n_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            n_active -= 1
            nexts = it.cycle(it.islice(nexts, n_active))


def partition(pred, iterable):
    # partition(is_odd, range(8)) -> 0 2 4 6; 1 3 5 7
    t1, t2 = it.tee(iterable)
    return it.filter_false(pred, t1), filter(pred, t2)


def before_after(predicate, it):
    pass
