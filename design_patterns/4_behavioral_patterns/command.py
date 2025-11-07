from abc import ABC, abstractmethod


def main():
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    remote = RemoteControl()
    remote.set_command(light_on)
    remote.press_button()
    remote.set_command(light_off)
    remote.press_button()
    

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def turn_on(self):
        print('Light is on')

    def turn_off(self):
        print('Light is off')


class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()


class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        if self._command is not None:
            self._command.execute()


if __name__ == '__main__':
    main()
