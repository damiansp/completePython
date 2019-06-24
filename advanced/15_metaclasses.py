class LoadableSaveable(type):
    def __init__(cls, classname, bases, dictionary):
        super().__init__(classname, bases, dictionary)
        assert hasattr(cls, 'load') and isinstance(
            getattr(cls, 'load'), collections.Callable), \
            ('class' + classname + 'must provide a load() method')
        assert hasattr(cls, 'save') and isinstance(
            getattr(cls, 'save'), collections.Callable), \
            ('class' + classname + 'musta provide a save() method')


def Bad(metaclass=Meta.LoadableSaveable):
    def some_method(self):
        pass
             

def Good(metaclass=Meta.LoadableSaveable):
    def load(self):
        pass

    def save(self):
        pass

g = Good()
