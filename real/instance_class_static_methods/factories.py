from math import pi


class Pizza:
    def __init__(self, size, ingredients):
        self.ingredients = ingredients
        self.size = size
        self.radius = {'s': 10,
                       'm': 12,
                       'l': 16,
                       'xl': 18}[size]

    def __repr__(self):
        return f'Pizza({self.size}, {self.ingredients!r})'

    @classmethod
    def margherita(cls, size):
        return cls(size, ['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls, size):
        return cls(size, ['mozzarrella', 'tomoatoes', 'ham'])

    @staticmethod
    # a poor example, but a method that does not need to change either the class
    # or instance state
    def area(r):
        return pi * r**2


order1 = Pizza.margherita('m')
order2 = Pizza.prosciutto('xl')
print(order1)
print(order2)
print(order1.area(order1.radius))
print(order2.area(order2.radius))
