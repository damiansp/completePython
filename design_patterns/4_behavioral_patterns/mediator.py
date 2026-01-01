from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._comp1 = component1
        self._comp1.mediator = self
        self._comp2 = component2
        self._comp2.mediator = self

    def notify(self, sender, event):
        pass  # TODO
