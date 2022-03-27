import uuid


def set_class_name_and_id(cls):
    cls.name = str(cls)
    cls.idn = uuid.uuid4()
    return cls


@set_class_name_and_id
class SomeClass:
    pass


print(SomeClass.name)
print(SomeClass.idn)


class CountCalls:
    def __init__(self, f):
        self.f = f
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.f(*args, **kwargs)


@CountCalls
def greet_em():
    print('Hello')

greet_em()
greet_em()
print(greet_em.calls)


def is_admin(f):
    def wrapper(*arg, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('Access Denied')
        return f(*args, **kwargs)

    return wrapper


def fubar(username='anon'):
    '''Hammer shit'''
    pass

print(fubar.__doc__) # Hammer shit
print(fubar.__name__) # fubar


@is_admin
def fubar(username='anon'):
    '''Hizammer shizit'''
    pass

print(fubar.__doc__) # None :(
print(fubar.__name__) # wrapper :(
