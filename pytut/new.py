class Person:
    def __init__(self, name):
        self.name = name


person = Person('John')  # This is equivalent to:

person = object.__new__(Person, 'John')
person.__init__('John')


person = object.__new__(Person, 'John')
print(person.__dict__)  # {}
person.__init__('John')
print(person.__dict__)  # {‘name': 'John'}


class Person:
    def __new__(cls, name):
        print(f'Creating a new {cls.__name__} object...')
        obj = object.__new__(cls)
        return obj

    def __init__(self, name):
        print(f'Initializing a Person object with name {name}...')
        self.name = name


person = Person('John')

