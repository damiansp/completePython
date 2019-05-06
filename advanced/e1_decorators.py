# Code here adapted from https://realpython.com/primer-on-python-decorators/

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

# greet('Señor Montelbaum') # TypeError: wrapper() takes 0 positional arguments


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
