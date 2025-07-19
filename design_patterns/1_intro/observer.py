class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify()


class Observer:
    def update(self, state):
        pass


class ConcreteObserver(Observer):
    def update(self, state):
        print(f'State changed to {state}')


subj = Subject()
obs1 = ConcreteObserver()
obs2 = ConcreteObserver()
subj.attach(obs1)
subj.attach(obs2)
subj.set_state('New State')
