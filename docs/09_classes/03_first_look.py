# 2. Class Objects
class MyClass:
    '''A simple example class'''
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()


class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def __str__(self):
        op = '+' if self.i >= 0 else '-'
        return f'{self.r} {op} {abs(self.i)}i'

x = Complex(3., -4.5)
print(x)



# 5. Class and Instance Variables
class Dog:
    kind = 'canine' # class var, shared by all instances

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def learn_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.learn_trick('shake')
d.learn_trick('sit')
print(d.name, d.kind, d.tricks) # Fido canine [shake, sit]
print(e.name, e.kind) # Buddy canine



# 4. Random Remarks
# instance attributes override class attributes
class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region) # storage west
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region) # storage east


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add2(self, x):
        self.add(x)
        self.add(x)


