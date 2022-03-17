import abc


class AbstractClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_stuff(self):
        pass

    @property
    @abc.abstractmethod
    def stuff(self):
        pass

class BadSubclass(AbstractClass):
    pass


try:
    bad_instance = BadSubclass()
except TypeError as e:
    print(e)


class Legit(AbstractClass):
    def __init__(self, stuff):
        self._stuff = stuff

    @property
    def stuff(self):
        return self._stuff
        
    def do_stuff(self):
        print(f'{self._stuff} is done, dude.')


legit = Legit('my_stuff')
legit.do_stuff()
print(legit.stuff)
