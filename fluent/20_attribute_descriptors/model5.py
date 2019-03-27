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
