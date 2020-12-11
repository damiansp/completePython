# 1. Multiple Inheritance
class Speaker:
    def __init__(self, name='Speaker'):
        print('Initializing Speaker with name:', name)
        self.name = name
        
    def speak(self):
        print(f'{self.name}: Hello')

        
class Walker:
    def __init__(self, name='Walker', speed=7):
        print('Initializing Walker with name:', name)
        self.name = name
        self.speed = speed
        
    def walk(self):
        print(f'{self.name} started walking at {self.speed} mph.')


class Person(Speaker, Walker):
    def __init__(self, name, speed):
        print('Initializing Person with name:', name)
        super().__init__(name) # only initializes Speaker
        self.speed = speed
        self.speak()


bob = Person('Bob Dobolina', 5)
bob.walk()
print(bob.name)
