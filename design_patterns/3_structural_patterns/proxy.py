from abc import ABC, abstractmethod


def main():
    print('Loading and displaying image through proxy')
    image = ImageProxy('photo.jpg')
    client_code(image)
    print('...and again')
    client_code(image)


def client_code(image):
    print('Client: I am unaware of the proxy.')
    image.display()
    

class Image(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f'Loading {self.filename} from disk')

    def display(self):
        print(f'Displaying {self.filename}')


class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


if __name__ == '__main__':
    main()
