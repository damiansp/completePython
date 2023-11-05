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


class SquareNumber(int):
    def __new__(cls, val):
        return super().__new__(cls, val ** 2)


x = SquareNumber(3)
print('x:', x)
print('int:', isinstance(x, int))


#class BadSquareNumber(int):
#    def __init__(self, val):
#        super().__init__(val ** 2)  # TypeError: int.__init__ takes exactly 1 arg (self)


class Persona:
    def __new__(cls, name, surname):
        obj = super().__new__(cls)
        obj.name = name
        obj.surname = surname
        obj.full_name = f'{name} {surname.upper()}'
        return obj

person = Persona('John Michael', 'Doe')
print(person.full_name)
print(person.__dict__)
