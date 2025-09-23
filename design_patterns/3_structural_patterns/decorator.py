from abc import ABC, abstractmethod


def main():
    simple_coffee = SimpleCoffee()
    print(f'{simple_coffee.get_description()}: ${simple_coffee.get_cost()}')
    milk_coffee = Milk(simple_coffee)
    print(f'{milk_coffee.get_description()}: ${milk_coffee.get_cost()}')
    milk_sugar_coffee = Sugar(Milk(simple_coffee))
    print(
        f'{milk_sugar_coffee.get_description()}: '
        f'${milk_sugar_coffee.get_cost()}')
                             

# Component
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self):
        return 5

    def get_description(self):
        return 'Simple Coffee'


# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()


# Concrete Decorators
class Milk(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 2

    def get_description(self):
        return f'{self._coffee.get_description()} + Milk'


class Sugar(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 1

    def get_description(self):
        return f'{self._coffee.get_description()} + Sugar'


if __name__ == '__main__':
    main()
