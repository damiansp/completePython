from abc import ABC, abstractmethod


def main():
    c1 = Comp1()
    c2 = Comp2()
    med = ConcreteMediator(c1, c2)
    print('Client triggers op A')
    c1.do_a()
    print('\nClient triggers op D')
    c2.do_d()
    

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
        if event == 'D':
            print('Mediator reacts on A and triggers the following:')
            self._comp2.do_c()
        elif event == 'D':
            print('Mediator reacts on D and triggers the following:')
            self._comp2.do_b()
            self._comp2.do_c()


class BaseComponent:
    def __init__(self, mediator=None):
        self._med = mediator

    @property
    def mediator(self):
        return self._med

    @mediator.setter
    def mediator(self, mediator):
        self._med = mediator


class Comp1(BaseComponent):
    def do_a(self):
        print('Comp1 does A')
        self.mediator.notify(self, 'A')

    def do_b(self):
        print('Comp1 does B')


class Comp2(BaseComponent):
    def do_c(self):
        print('Comp2 does C')

    def do_d(self):
        print('Comp2 does D')
        self.mediator.notify(self, 'D')


if __name__ == '__main__':
    main()
