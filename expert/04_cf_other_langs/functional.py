from dataclasses import dataclass
from functools import partial, reduce, wraps
from itertools import count
import math

from flask import g, request, redirect, url_for


def get_circle_area(r):
    return math.pi * r**2


R = 42
print(get_circle_area(R))
print(get_circle_area)
print(get_circle_area.__class__)
print(get_circle_area.__name__)

get_c_area = lambda r: math.pi * r**2
print()
print(get_c_area(R))
print(get_c_area)
print(get_c_area.__class__)
print(get_c_area.__name__)


@dataclass
class Person:
    age: int
    weight: int
    name: str


al = Person(40, 190, 'Al')
bob = Person(45, 170, 'Bob')
cris = Person(47, 110, 'Cris')
dan = Person(38, 120, 'Dan')
people = [al, bob, cris, dan]
print(sorted(people, key=lambda person: person.age))

sq_map = map(lambda x: x**2, range(10))
print(sq_map)
print(list(sq_map))

mapped = list(map(print, range(5), range(4), range(5)))
print(mapped)

evens = filter(lambda n: n % 2 == 0, range(10))
odds = filter(lambda n: n % 2 == 1, range(10))
print(list(evens))
print(list(odds))

animals = ['giraffe', 'snake', 'lion', 'squirrel']
s_animals = filter(lambda animal: animal.startswith('s'), animals)
print(list(s_animals))
      
print(reduce(lambda a, b: a + b, [2, 2]))
print(reduce(lambda a, b: a + b, [2, 2, 4]))
print(reduce(lambda a, b: a + b, range(100)))

#for i in count(): # counts integers forever
#    print('i:', i)

seq = map(lambda x: x**2, count()) # a generator
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


# Partials
pow2 = partial(pow, 2)
print(pow2(3))
print(pow2(5))
print(pow2(10))


# Generators
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
for i in fibonacci():
    print(i, end=' ')
    if i > 10:
        break


# Decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function

# Flask Ex:
#@app.route('/secret_page')
#@login_required
#def secret_page():
#    pass # ...

