from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity



class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        discount = 0 if self.promotion is None\
                   else self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())



class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        '''Return discount as a positive dollar amount'''



class FidelityPromo(Promotion):
    '''5% discount for customers with 1000+ fidelity points'''
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0



class BulkItemPromo(Promotion):
    '''10% discount for each LineItem with 20+ units'''
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount



class LargeOrderPromo(Promotion):
    '''7% discount for orders with 10+ distinct items'''
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0



john = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(20)]
print(Order(john, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))
print(Order(john, banana_cart, BulkItemPromo()))
print(Order(ann, long_order, LargeOrderPromo()))
print(Order(john, cart, LargeOrderPromo()))
