from abc import ABC, abstractmethod


# Component
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_size(self):
        pass


# Leaf
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self):
        print(f'File: {self.name}')

    def get_sie(self):
        return self.size


# Composite
