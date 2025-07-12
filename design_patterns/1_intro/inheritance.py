class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f'{self.name}: Woof!'


class Cat(Animal):
    def speak(self):
        return f'{self.name}: Meow!'


dog = Dog('Milo')
cat = Cat('Otis')
print(dog.speak())
print(cat.speak())


    
              
