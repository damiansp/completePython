from pprint import pprint


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
        # define __init__, etc
        setattr(class_obj, '__init__', Data.init(class_obj))
        setattr(class_obj, '__repr__', Data.repr(class_obj))
        setattr(class_obj, '__eq__', Data.eq(class_obj))
        setattr(class_obj, '__hash__', Data.hash(class_obj))
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
    def repr(class_obj):
        def _repr(self):
            prop_vals = (getattr(self, prop) for pros in class_obj.props)
            prop_kv = (f'{k}={v}' for k, v in zip(class_obj.props, prop_vals))
            prop_kv_str = ', '.join(prop_kv)
            return f'{class_obj.__name__}({prop_kv_str})'

        return _repr

    @staticmethod
    def eq(class_obj):
        def _eq(self, other):
            if not isinstance(other, class_obj):
                return False
            self_vals = [getattr(self, prop) for prop in class_obj.props]
            other_vals = [getattr(self, prop) for prop in other.props]
            return self_vals == other_vals

        return _eq

    @staticmethod
    def hash(class_obj):
        def _hash(self):
            vals = (getattr(self, prop) for prop in class_obj.props)
            return hash(tuple(vals))

        return _hash

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


def data(cls):
    return Data(cls.__name__, cls.__bases__, dict(cls.__dict__))


@data
class Employee:
    props = ['name', 'job_title']
