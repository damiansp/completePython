import itertools


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end # None: arbitrarily long

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step*index

            
# Functionally identical:
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step*index


gen = itertools.count(1, 0.5)
print(nex(gen)) # 1
print(nex(gen)) # 1.5
print(nex(gen)) # 2.0
print(nex(gen)) # 2.5

# list(count()) # -> infinite: will eventually crash for want of memory
gen = intertools.takewhile(lambda n: n < 5, itertools.count(1, 0.5))
print(list(gen)) # [1, 1.5, 2.0, 2.5, ..., 4.0, 4.5]


def arith_prog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


