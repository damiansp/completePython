import abc

class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        '''Add items from an iterable'''

    @abc.abstractmethod
    def pick(self):
        '''
        Remove item at random, returning it.
        This method should raise LookupError when instance is empty.
        '''

    def loaded(self):
        '''True if at least 1 item, else False'''
        return bool(self.inspect())

    def inspect(self):
        '''Return a sorted tuple with the items currently inside'''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
