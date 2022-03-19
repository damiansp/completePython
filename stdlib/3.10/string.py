# Format string syntax
class Person:
    def __init__(self, name):
        self.name = name

worker = Person('Bob Dobolina')
fruits = ['tangerine', 'durian', 'kiwi']

print('First, thou shalt count to {0}'.format('three'))
print('Bring out {}'.format('Rodrick'))
print('From {} to {}'.format('here', 'there'))
print('My quest is {name}'.format(name='the grail'))
print('The worker is named: {0.name}'.format(worker))
print('My favorite fruit is {fruits[2]}'.format(fruits=fruits))
print('{0!s} is right out!'.format(5))
