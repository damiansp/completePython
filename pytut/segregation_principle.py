from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Aircraft(Vehicle):
    def go(self):
        print('Taxiing')

    def fly(self):
        print('Flying')


class Car(Vehicle):
    def go(self):
        print('Driving')

    # boo: should not need to implement this
    def fly(self):
        print('Not a flying car')


# Better implementation
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Aircraft(Vehicle):
    @abstractmehtod
    def fly(self):
        pass


class Airplane(Aircraft):
    def go(self):
        print('Taxiing')

    def fly(self):
        print('Flying')


class Car(Vehicle):
    def go(self):
        print('Driving')
