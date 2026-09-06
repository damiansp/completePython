from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass


class RedLight(TrafficLightState):
    def change(self, traffic_light):
        print('Red light - Stop')
        traffic_light.set_state(GreenLight())
