from abc import ABC, abstractmethod


def main():
    # client code
    root = Directory('Root')
    docs = Directory('Docs')
    pics = Directory('Pics')
    f1 = File('report.docx', 1000)
    f2 = File('img.jpg', 2000)
    docs.add(f1)
    pics.add(f2)
    root.add(docs)
    root.add(pics)
    root.display()
    print(f'Total size: {root.get_size()} bytes')


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

    def get_size(self):
        return self.size


# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self):
        print(f'Directory: {self.name}')
        for child in self.children:
            child.display()

    def get_size(self):
        return sum(child.get_size() for child in self.children)


if __name__ == '__main__':
    main()
