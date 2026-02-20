import copy


def main():
    o = Originator()
    c = Caretaker(o)
    o.set_state('k1', 'v1')
    c.backup()
    o.set_state('k2', 'v2')
    c.backup()
    o.set_state('k1', 'new v')
    print(o.get_state())
    c.undo()
    print(o.get_state())
    c.undo()
    print(o.get_state())


class Memento:
    def __init__(self, state):
        self._state = copy.deepcopy(state)

    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = {}

    def set_state(self, k, v):
        self._state[k] = v

    def get_state(self):
        return self._state

    def save(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.get_state()


class Caretaker:
    def __init__(self, originator):
        self._originator = originator
        self._history = []

    def backup(self):
        self._history.append(self._originator.save())

    def undo(self):
        if not self._history:
            return
        memento = self._history.pop()
        self._originator.restore(memento)


if __name__ == '__main__':
    main()
