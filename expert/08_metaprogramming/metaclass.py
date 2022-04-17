# General syntax
def method(self):
    return 1


MyClass = type('MyClass', (), {'method': method})


# same as:
class MyClass:
    def method(self):
        return 1

# 'type' is the implicit metaclass
class ClassWithMetaclass(metaclass=type):
    pass


# Common template
class Metaclass(type):
    def __new__(mcs, name, bases, namespace):
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, naemespace, **kwargs):
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class Klass(metaclass=MetaClass, extra='value'):
    pass

