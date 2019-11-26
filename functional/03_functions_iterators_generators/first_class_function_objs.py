import collections


class Mersennel(collections.Callable):
    def __init__(self, algorithm):
        self.pow2 = algorithm

    def __call__(self, arg):
        return self.pow2(arg) - 1


# Different algos to calculate a power of 2
def shifty(b):
    # return 2 ** b efficiently
    return 1 << b


def multy(b):
    if b == 0:
        return 1
    return 2*multy(b - 1)


def faster(b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return 2 * faster(b - 1)
    t = faster(b // 2)
    return t * t


mls = Mersennel(shifty)
mlm = Mersennel(multy)
mlf = Mersennel(faster)

