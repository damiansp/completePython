'A metaclass is a class that creates other classes'
from pprint import pprint


class Person:  # same as: class Person(object, metaclass=type):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Human(type):
    def __new__(mcs, name, bases, class_dict):
        class_ = super().__new__(mcs, name, bases, class_dict)
        class_.freedom = True
        return class_


class Person(object, metaclass=Human):
    def __init__(self, name, age):
        self.name = name
        self.age = age


pprint(Person.__dict__)


# Metaclass Params
class Human(type):
    def __new__(mcs, name, bases, class_dict, **kwargs):
        class_ = super().__new__(mcs, name, bases, class_dict)
        if kwargs:
            for name, val in kwargs.items():
                setattr(class_, name, val)
        return class_


class American(
        object, metaclass=Human, country='USA', gov='capitalist democracy'):
    def __init__(self, name, age):
        self.name = name
        self.age = age


pprint(American.__dict__)
