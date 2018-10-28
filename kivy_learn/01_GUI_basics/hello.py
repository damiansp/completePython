import kivy
from kivy.app import App
from kivy.uix.button import Label

kivy.require('1.10.0')


class HelloApp(App):
    def build(self):
        return Label(text="Hello, World!")


if __name__ == '__main__':
    HelloApp().run()


