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





