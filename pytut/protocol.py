from typing import List, Protocol


class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


def get_total(items: List[Product]) -> float:
    return sum([item.quantity * item.price for item in items])



class Item(Protocol):
    quantity: float
    price: float


def get_total(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])


total = get_total([
    Product('A', 10, 150),
    Product('B', 5, 25.75)])
print(total)


class Thingy:
    def __init__(self, quantity: float, price: float):
        self.quantity = quantity
        self.price = price


total = get_total([
    Product('A', 10, 150),
    Product('B', 5, 25.75),
    Thingy(12, 12.12)])
print(total)
                        
