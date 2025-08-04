import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_obj(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self):
        self.make = 'Ford'
        self.model = 'Mustang'
        self.color = 'red'

    def __str__(self):
        return f'{self.make} {self.model} in {self.color}'

def main():
    car_proto = Prototype()
    car = Car()
    print(car)
    car_proto.register_object('car', car)
    car2 = car_proto.clone('car')
    print(car2)
    car3 = car_proto.clone('car', color='blue', model='GT')
    print(car3)


if __name__ == '__main__':
    main()


