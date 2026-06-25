def main():
    subj = Subject()
    obs_a = ConcreteObserverA()
    subj.attach(obs_a)
    obs_b = ConcreteObserverB()
    subj.attach(obs_b)
    subj.set_state(123)
    subj.detach(obs_a)
    subj.set_state(456)


class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for o in self._observers:
            o.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state


class Observer:
    def update(self, state):
        pass


class ConcreteObserverA(Observer):
    def update(self, state):
        print(f'ConcreteObserverA: Reacted to event. State {state}')


class ConcreteObserverB(Observer):
    def update(self, state):
        print(f'ConcreteObserverB: Reacted to event. State {state}')


if __name__ == '__main__':
    main()
