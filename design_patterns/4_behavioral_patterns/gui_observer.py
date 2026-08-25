def main():
    button = Button()
    observer = ClickObserver()
    button.attach(observer)
    button.click()
    

class Button:
    def __init__(self):
        self._observers = []
        self._clicked = False

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def click(self):
        self._clicked = True
        self.notify()


class ClickObserver:
    def update(self, button):
        print('Button clicked!')


if __name__ == '__main__':
    main()
    
