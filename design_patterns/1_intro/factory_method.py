class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return 'Woof!'


class Cat(Animal):
    def speak(self):
        return 'Meow!'


def animal_factory(animal_type):
    return {
        'dog': Dog,
        'cat': Cat
     }[animal_type]()


dog = animal_factory('dog')
cat = animal_factory('cat')
print(dog.speak())
print(cat.speak())

pig = animal_factory('pig')
