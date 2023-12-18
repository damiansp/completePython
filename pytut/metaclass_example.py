from pprint import pprint


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        self._age = val

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(f'{self.name}, {self.age}')

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


class Prop:
    def __init__(self, attr):
        self._attr = attr

    def get(self, obj):
        return getattr(obj, self._attr)

    def set(self, obj, val):
        return setattr(obj, self._attr, val)

    def delete(self, obj):
        return delattr(obj, self._attr)


class Data(type):
    def __new__(mcs, name, bases, class_dict):
        class_obj = super().__new__(mcs, name, bases, class_dict)
        Data.define_property(class_obj)
        return class_obj
        # define __init__
        setattr(class_obj, '__init__', Data.init(class_obj))
        return class_obj

    @staticmethod
    def init(class_obj):
        def _init(self, *obj_args, **obj_kwargs):
            if obj_kwargs:
                for prop in class_obj.props:
                    if prop in obj_kwargs.keys():
                        setattr(self, prop, obj_kwargs[prop])
            if obj_args:
                for kv in zip(class_obj.props, obj_args):
                    setattr(self, kv[0], kv[1])

        return _init

    @staticmethod
    def define_property(class_obj):
        for prop in class_obj.props:
            attr = f'_{prop}'
            prop_obj = property(
                fget=Prop(attr).get,
                fset=Prop(attr).set,
                fdel=Prop(attr).delete)
            setattr(class_obj, prop, prop_obj)
        return class_obj


class Person(metaclass=Data):
    props = ['name', 'age']


pprint(Person.__dict__)
p = Person('John Doe', age=25)
print(p.__dict__)
