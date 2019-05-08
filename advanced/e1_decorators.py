# Code here adapted from https://realpython.com/primer-on-python-decorators/
import functools
import time


def my_decorator(f):
    def wrapper():
        print(f'Before {f.__name__} is called')
        f()
        print(f'After {f.__name__} is called')
    return wrapper


def say_hi():
    print('Hi')


say_hi = my_decorator(say_hi)
say_hi()


@my_decorator
def say_bye():
    print('Bye')

    
say_bye()


def do_twice(f):
    def wrapper():
        f()
        f()
    return wrapper


@do_twice
def say_yo():
    print('Yo')


say_yo()



# Passing args

@do_twice
def greet(name):
    print(f'Hello {name}')

# greet('Señor Montalban') # TypeError: wrapper() takes 0 positional arguments


def do_twice_new(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return wrapper


@do_twice_new
def say_hey():
    print('Hey!')


@do_twice_new
def salute(title):
    print(f'Hello, {title}')

say_hey()
salute('Doctor')



# Returning vals

def do_twice_and_return(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return f(*args, **kwargs)
    return wrapper


@do_twice_and_return
def return_greeting(name):
    print('Creating greeting')
    return f'Hi {name}'


hi_adam = return_greeting('Adam')
print(hi_adam)


def do_twice_clean(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return f(*args, **kwargs)
    return wrapper


@do_twice_clean
def say_clean():
    print('So fresh and so clean!')

say_clean()
print(say_clean.__name__)


def timer(f):
    '''print the runtime of the decorated function f'''
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = f(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f'Finished {f.__name__!r} in {runtime:.4f}s')
        return val
    return wrapper


@timer
def waste_time(n_times):
    for _ in range(n_times):
        sum([i**2 for i in range(10000)])


waste_time(1)
waste_time(2)
waste_time(4)

