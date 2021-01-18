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

