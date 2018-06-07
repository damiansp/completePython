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
                   else self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    '''5% discount for customers w 1000+ fidelity points'''
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    '''10% discount for each LineItem with 20+ units'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    '''7% discount on orders with 10+ distinct items'''
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


#promos = [fidelity_promo, bulk_item_promo, large_order_promo]
promos = [globals()[name] for name in globals()
          if name.endswith('_promo') and name != 'best_promo']

# or if promotions are bundled in a module:
#promos = [func for name, func in inspect.getmembers(promotions,
#                                                    inspect.isfunction)]

def best_promo(order):
    '''Select best discount available'''
    return max(promo(order) for promo in promos)


john = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(20)]
print(Order(john, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))
print(Order(john, banana_cart, bulk_item_promo))
print(Order(ann, long_order, large_order_promo))
print(Order(john, cart, large_order_promo))
