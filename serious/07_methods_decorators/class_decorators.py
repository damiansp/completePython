import functools
import inspect
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


WRAPPER_ASSIGNMENTS = (
    '__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
WRAPPER_UPDATES = ('__dict__',)


def update_wrapper(
        wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES
):
    for attr in assignied:
        try:
            val = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, val)
    for attr in updated:
        getattr(wrapper, attr).update(getttr(wrapped, attr, {}))
    wrapper.__wrapped__ = wrapped
    return wrapper


def fubar(username='user'):
    '''Hammer time!'''
    pass

fubar = functools.update_wrapper(is_admin, fubar)
print(fubar.__name__)  # fubar
print(fubar.__doc__)   # Hammer time!


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('Access Denied')
        return f(*args, **kwargs)

    return wrapper


class Store:
    @check_is_admin
    def get_food(self, username, food):
        '''Get food from storage'''
        return self.storage.get(food)


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        if func_arg.get('username') != 'admin':
            raise Exception('Access Denied')
        return f(*args, **kwargs)

    return wrapper


@check_is_admin
def get_food(username, variety):
    return variety + ', nom nom nom'


class Pizza:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


print(Pizza.get_size)  # <function Pizza.get_size at 0x...>
try:
    print(Pizza.get_size())  # err: must belong to an instance
except:
    print(Pizza.get_size(Pizza(42)))  # or
    print(Pizza(42).get_size())

print(Pizza(42).get_size)
# <bound method Pizza.get_size of <__main__.Pizza object at 0x7fd5f0378af0>>

ps = Pizza(42).get_size
print(ps())  # 42
print(ps.__self__)  # <__main__.Pizza object at 0x7fdfa0298af0>


# Static methods
class Pizza:
    @staticmethod
    def mix(x, y):
        return x + y

    def cook(self):
        return self.mix('cheese ', 'veggies ')

print(Pizza().cook is Pizza().cook)  # False
print(Pizza().mix is Pizza().mix)    # True
print(Pizza().mix is Pizza.mix)      # True


# Class methods
class Pizza:
    rad = 42

    @classmethod
    def get_radius(cls):
        return cls.rad


print(Pizza.get_radius)
# <bound method Pizza.get_radius of <class '__main__.Pizza'>>
print(Pizza().get_radius)  # same
print(Pizza.get_radius is Pizza().get_radius)  # False


'''
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_veggies())
'''

