from abc import ABC, abstractmethod


def main():
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    remote = RemoteControlWithUndo()
    remote.press_button(light_on)
    remote.press_button(light_off)
    remote.undo()
    remote.undo()
    

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class UndoableCommand(Command):
    @abstractmethod
    def undo(self):
        pass


class Light:
    def turn_on(self):
        print('Light is on')

    def turn_off(self):
        print('Light is off')


class LightOnCommand(UndoableCommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

    def undo(self):
        self._light.turn_off()


class LightOffCommand(UndoableCommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

    def undo(self):
        self._light.turn_on()


class CommandHistory:
    def __init__(self):
        self._commands = []

    def push(self, command):
        self._commands.append(command)

    def pop(self):
        return self._commands.pop() if self._commands else None


class RemoteControlWithUndo:
    def __init__(self):
        self._history = CommandHistory()

    def press_button(self, command):
        command.execute()
        self._history.push(command)

    def undo(self):
        command = self._history.pop()
        if command:
            command.undo()


if __name__ == '__main__':
    main()
