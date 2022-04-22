import inflection
from typing import Any


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
class MetaClass(type):
    def __new__(mcs, name, bases, namespace):
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


#class Klass(metaclass=MetaClass, extra='value'):
#    pass


class RevealingMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, 'METACLASS __new__ called')
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, 'METACLASS __prepare__ called')
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, 'METACLASS __init__ called')
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, 'METACLASS __call__ called')
        return super().__call__(*args, **kwargs)


class RevealingClass(metaclass=RevealingMeta):
    def __new__(cls):
        print(cls, '__new__ called')
        return super().__new__(cls)

    def __init__(self):
        print(self, '__init__ called')
        super().__init__()


rc = RevealingClass()


# Example usage of __prepare__: allow camelCase function names to be used and
# automatically converted to snake_case
class FlexiCamelDict(dict):
    def __setitem__(self, key: str, value: Any):
        super().__setitem__(key, value)
        super().__setitem__(inflection.underscore(key), value)


class FlexiCamelMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        return FlexiCamelDict()


class User(metaclass=FlexiCamelMeta):
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def getDisplayName(self):
        return f'{self.firstName} {self.lastName}'

    def greetUser(self):
        return f'Hello, {self.getDisplayName()}!'


user = User('Bob', 'Dobolina')
print(user.get_display_name())  # !!
print(user.greet_user())
print(User.__dict__)
