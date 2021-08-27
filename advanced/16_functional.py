import functools
import operator
import os


print(list(map(lambda x: x**2, [1, 2, 3, 4]))) # [1 4 9 16]
print(map(lambda x: x**2, [1, 2, 3, 4])) # map object (an iterator)
print(list(filter(lambda x: x > 0, [-1, 1, -2, 2, -3, 3]))) # [1 2 3]
print(functools.reduce(lambda x, y: x * y, [1, 2, 3, 4]))   # 24
print(functools.reduce(operator.mul, [1, 2, 3, 4]))         # 24

files = os.listdir('.')
print(functools.reduce(
    operator.add,
    map(os.path.getsize, filter(lambda x: x.endswith('.py'), files))))
# same as
print(functools.reduce(
    operator.add,
    (os.path.getsize(x) for x in files if x.endswith('.py'))))

