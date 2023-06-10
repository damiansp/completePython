from enum import Enum, auto


class State(Enum):
    PENDING = 1
    FULFILLED = 2
    REJECTED = 3


class AutoState(Enum):
    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()

    def __str__(self):
        return f'{self.name(self.value)}'


for state in AutoState:
    print(state.name, state.value)


class SemiAutoState(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    PENDING = auto()
    FULFILLED = auto()
    REJECTED = auto()


for state in SemiAutoState:
    print(state.name, state.value)
