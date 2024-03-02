import math


def is_prime(n):
    int_sqrt = int(math.sqrt(n))
    for i in range(2, int_sqrt + 1):
        if (n / i).is_integer():
            return False
    return True


vals = [10_000_000, 10_000_019]
for val in vals:
    print(f'{val} is prime: {is_prime(val)}')


def is_prime2(n):
    int_sqrt = int(math.sqrt(n))
    ns = range(2, int_sqrt + 1)
    for i in range(0, len(ns), 5):
        # not valid python, just vectorizing example
        res = (n / ns[i:(i + 5)]).is_integer()
        if any(res):
            return False
    return True

