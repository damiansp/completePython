class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        # cannot modify instance state, only class state
        return 'class method called', cls

    @staticmethod
    def staticmethod(): # no required params!
        return 'static method called'


obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

#print(MyClass.method()) # TypeError (no self arg)
print(MyClass.classmethod())
print(MyClass.staticmethod())


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'


print(Pizza(['cheese', 'pepperoni']))
