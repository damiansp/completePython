import numpy as np


class MyError(Exception):
    pass


def my_generator():
    yield 1
    yield 2
    yield 3


it = my_generator()
print(next(it)) # 1
print(next(it)) # 2
#print(it.throw(MyError('test error')))


def my_gen():
    yield 1
    try:
        yield 2
    except MyError:
        print('Got MyError')
    else:
        yield 3
    yield 4

it = my_gen()
print(next(it)) # 1
print(next(it)) # 2
print(it.throw(MyError('test error')))


class Reset(Exception):
    pass


def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


def should_reset():
    x = np.random.choice([1, 2, 3])
    return x == 3


def announce(remaining):
    print(f'{remaining} remaining')

    
def run():
    it = timer(8)
    while True:
        try:
            if should_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

run()
