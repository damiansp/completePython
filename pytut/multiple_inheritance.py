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


def main():
    fc = FlyingCar()
    fc.start()
    fc.drive()
    fc.fly()
    

if __name__ == '__main__':
    main()
