class Car:
    def start(self):
        print('Starting the car')
        
    def drive(self):
        print('Driving')


class Flyer:
    def start(self):
        print('Initializing flight sequence')
        
    def fly(self):
        print('Flying')


class FlyingCar(Flyer, Car):
    pass


class Car2:
    def __init__(self, door, wheel):
        self.door = door
        self.wheel = wheel

    def start(self):
        print('Starting the car')

    def go(self):
        print('Driving')


class Flyer2:
    def __init__(self, wing):
        self.wing = wing
        
    def start(self):
        print('Initializing flight sequence')
        
    def fly(self):
        print('Flying')


class FlyingCar2(Flyer2, Car2):
    def __init__(self, door, wheel, wing):
        super().__init__(wing=wing)
        self.door = door
        self.wheel = wheel


def main():
    fc = FlyingCar()
    fc.start()
    fc.drive()
    fc.fly()
    print(FlyingCar.__mro__)  # method resolution order

    fc2 = FlyingCar2('pulldown', 'rubber', 'aluminum alloy')
    fc2.start()
    

if __name__ == '__main__':
    main()
