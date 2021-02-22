class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field


foo = MyObject()
assert foo.public_field == 5
assert foo.get_private_field() == 10


try:
    print(foo.__private_field)
except BaseException as e:
    print(f'{type(e)}: {e}') # Attribute Error: MyObject has no attribute...


class MyOtherObject:
    def __init__(self):
        self.__private = 71

    @classmethod
    def get_instance_private(cls, instance):
        return instance.__private

bar = MyOtherObject()
assert MyOtherObject.get_instance_private(bar) == 71


class MyParentObj:
    def __init__(self):
        self.__private = 71

        
class MyChildObj(MyParentObj):
    def get_private(self):
        try:
            return self.__private
        except BaseException as e:
            return f'{type(e)}: {e}'


baz = MyChildObj()
print(baz.get_private()) # Attribute Error...

print(baz._MyParentObj__private) # 71
print(baz.__dict__)


class MyStringClass:
    def __init__(self, val):
        self.__val = val

    def get_val(self):
        return str(self.__val)

foo = MyStringClass(5)
print(foo.get_val()) # '5'

# not good for subclassing...
