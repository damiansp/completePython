from collections import namedtuple
from types import SimpleNamespace


def square():
    # Bad choice!
    global n
    n *= n

n = 4
square()
print('n:', n) # 16


def sq(n):
    return n * n

print(sq(4)) # 16
x = 4
x = sq(x)


def greet(name, counter):
    return f'Hi, {name}!', counter + 1

counter = 0
for person in ['Alice', 'Bob', 'Chuck']:
    greeting, counter = greet(person, counter)
    print(greeting)
    print('Counter:', counter)


ns = SimpleNamespace()
def sqr(instance):
    instance.n *= instance.n

ns.n = 4
sqr(ns)
print(ns.n) # 16


NS = namedtuple('NS', 'n')
ns = NS(4)
print(ns.n) # 4
#sqr(ns)    # AttributeError: can't set attribute


class NS:
    n = 4

ns = NS()
print(ns.n) # 4
sqr(ns)
print(ns.n) # 16 (instance attribute)
print(NS.n) # 4  (class attribute)
