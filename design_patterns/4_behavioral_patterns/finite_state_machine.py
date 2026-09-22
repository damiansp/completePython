from abc import ABC, abstractmethod
from time import sleep

GREEN_DUR = 10
YELLOW_DUR = 2
RED_DUR = 10


def main():
    tl = TrafficLight()
    for _ in range(6):
        tl.change()
        

class TrafficLight:
    def __init__(self):
        self._state = RedLight()

    def set_state(self, state):
        self._state = state

    def change(self):
        self._state.change(self)


class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass


class RedLight(TrafficLightState):
    def change(self, traffic_light):
        print('Red light - Stop')
        sleep(RED_DUR)
        traffic_light.set_state(GreenLight())


class YellowLight(TrafficLightState):
    def change(self, traffic_light):
        print('Yellow light - Prepare to stop if safe to do so')
        sleep(YELLOW_DUR)
        traffic_light.set_state(RedLight())


class GreenLight(TrafficLightState):
    def change(self, traffic_light):
        print('Green light - Go!')
        sleep(GREEN_DUR)
        traffic_light.set_state(YellowLight())


if __name__ == '__main__':
    main()
