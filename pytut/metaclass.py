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
