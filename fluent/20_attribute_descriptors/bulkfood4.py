class Quantity:
    __counter = 0 # Counts no. of Quantity instances
    
    def __init__(self):
        cls = self.__class__ # reference to Quantity class
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f'_{prefix}#{index}' # unique for each instance
        cls.__counter += 1

    def __get__(self, instance, owner):
        # owner: reference to the managed class (LineItem)
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# Test
coconuts = LineItem('Brazilian coconut', 20, 17.95)
raisins = LineItem('Sun-dried raising', 5, 4.47)
print(coconuts.weight, coconuts.price) # (20, 17.95)

print(getattr(raisins, '_Quantity#0'), getattr(raisins, '_Quantity#1'))
# (5, 4.47)

print(LineItem.price) # <__main__.Quantity object at 0x108b532e8>
