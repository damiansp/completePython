from abc import ABC, abstractmethod


def main():
    ctx = Context(StateA())
    print(ctx.request())
    ctx.transition_to(StateB())
    print(ctx.request())


class State(ABC):
    @abstractmethod
    def handle(self):
        pass


class StateA(State):
    def handle(self):
        return 'State A behavior'


class StateB(State):
    def handle(self):
        return 'State B behavior'


class Context:
    def __init__(self, state: State) -> None:
        self._state = state

    def transition_to(self, state: State):
        print(f'Context: Transitioning to {type(state).__name__}')
        self._state = state

    def request(self):
        return self._state.handle()


if __name__ == '__main__':
    main()
