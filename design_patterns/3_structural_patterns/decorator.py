from abc import ABC, abstractmethod


# Component
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


# Concrete Component
