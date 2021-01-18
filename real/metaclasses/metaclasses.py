class Foo:
    pass

obj = Foo()
print(obj.__class__) # <class '__main__.Foo'>
print(type(obj))     # <class '__main__.Foo'>
print(obj.__class__ is type(obj)) # True


n = 5
d = {'x': 1, 'y': 2}
x = Foo()

for obj in (n, d, x, 7):
    print(type(obj) is obj.__class__) # T, T, T, T


Foo = type('Foo', (), {})
x = Foo()
print(x) # <__main__.Foo obj at 0x...>

Bar = type('Bar', (Foo,), dict(attr=100))
x = Bar()
print(x.attr) # 100
print(x.__class__) # <class '__main__.Bar'>
print(x.__class__.__bases__) # <class '__main__.Foo'>


Foo = type('Foo', (), {'attr': 100, 'attr_val': lambda x: x.attr})
x = Foo()
print(x.attr) # 100
print(x.attr_val()) # 100


class Foo:
    attr = 100

    def attr_val(self):
        return self.attr

x = Foo()
print(x.attr) # 100
print(x.attr_val()) # 100


def f(obj):
    print('attr =', obj.attr)


Foo = type('Foo', (), {'attr': 100, 'attr_val': f})
x = Foo()
print(x.attr) # 100
x.attr_val()  # 100


class Foo:
    attr = 100
    attr_val = f

x = Foo()
print(x.attr) # 100
x.attr_val()  # 100



# Custom Metaclasses
class Foo:
    pass

f = Foo()


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new
f = Foo()
print(f.attr) # 100
g = Foo()
print(g.attr) # 100


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class Foo(metaclass=Meta):
    pass

print(Foo.attr) # 100


class Bar(metaclass=Meta):
    pass

class Qux(metaclass=Meta):
    pass

print(Bar.attr, Qux.attr) # 100, 100


class Foo:
    def __init__(self):
        self.attr = 100


x = Foo()
print(x.attr) # 100

y = Foo()
print(y.attr) # 100


# Class factory
class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100

class X(metaclass=Meta):
    pass

print(X.attr) # 100



