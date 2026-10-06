from abc import ABC, abstractmethod
from time import sleep

DUR = 3


def main():
    o = Order()
    for _ in range(4):
        o.process()
        sleep(DUR)


class OrderState(ABC):
    @abstractmethod
    def process(self, order):
        pass


class NewOrder(OrderState):
    def process(self, order):
        print('Processing new order')
        order.set_state(PaymentPending())


class PaymentPending(OrderState):
    def process(self, order):
        print('Payment received')
        order.set_state(Shipping())


class Shipping(OrderState):
    def process(self, order):
        print('Order shipped')
        order.set_state(Delivered())


class Delivered(OrderState):
    def process(self, order):
        print('Order delivered')


class Order:
    def __init__(self):
        self._state = NewOrder()

    def set_state(self, state):
        self._state = state

    def process(self):
        self._state.process(self)


if __name__ == '__main__':
    main()
