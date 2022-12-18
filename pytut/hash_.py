class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('John', 22)
p2 = Person('Jane', 22)
print(hash(p1))
print(hash(p2))


class Clone(Person):
    def __eq__(self, other):
        return isinstance(other, Clone) and self.age == other.age

try:
    print(hash(Clone('John', 22)))
except TypeError as e:
    print(e)
    
try:
    army = {Person('John', 22), Person('Jane', 22)}
except TypeError as e:
    print(e)

try:
    clone_army = {Clone('John', 22), Clone('Jane', 22)}
except TypeError as e:
    print(e)


class HashClone:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # make hashed fields immutable

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, HashClone) and self.age == other.age
    
    def __hash__(self):
        return hash(self.age)


    



