from collections import abc


class Appliance(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, model, price):
        self.__model = model
        self.price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    price = abc.abstractproperty(get_price, set_price)

    @property
    def model(self):
        return self.__model


class Cooker(Appliance):
    def __init__(self, model, price, fuel):
        super().__init__(model, price)
        self.fuel = fuel
        price = property(lambda self: super().price,
                         lambda self, price: super().set_price(price))


class TextFilter(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def is_transformer(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError()


class CharCounter(TextFilter):
    @property
    def is_transformer(self):
        return False

    def __call__(self, text, chars):
        count = 0
        for c in chars:
            count += 1
        return count

    
vowel_counter = CharCounter()
print(vowel_counter('dog fish and cat fish', 'aeiou'))
    
