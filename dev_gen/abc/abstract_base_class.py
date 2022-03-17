import abc


class AbstractClass(metaclass=abc.ABCMeta):
    def abstract_func(self):
        return None

print(AbstractClass.register(dict))  # <class 'dict'>

AbstractClass.register(dict)
print(issubclass(dict, AbstractClass))  # True


class MySequence(metaclass=abc.ABCMeta):
    pass

MySequence.register(list)
MySequence.register(tuple)
a = [1, 2, 3]
b = ('x', 'y', 'z')
print(isinstance(a, MySequence))  # True
print(isinstance(b, MySequence))  # True
print(isinstance(object(), MySequence))  # False


class CustomListLikeObjCls(object):
    pass

MySequence.register(CustomListLikeObjCls)
print(issubclass(CustomListLikeObjCls, MySequence))  # True


@MySequence.register
class AnotherListLikeObjCls(object):
    pass

print(issubclass(AnotherListLikeObjCls, MySequence))  # True
      

class HookingClass(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, other):
        print('subclass hook:', other)
        hookmethod = getattr(other, 'hookmethod', None)
        return callable(hookmethod)


class SubClass:
    def hookmethod(self):
        pass


class UncertainClass:
    @staticmethod
    def hookmethod():
        pass

    
class NormalClass:
    hookmethod = 'not a method'


print('\nStarting hook stuff:')
for c in [SubClass, UncertainClass, NormalClass]:
    print(issubclass(c, HookingClass))  # True, True, False
