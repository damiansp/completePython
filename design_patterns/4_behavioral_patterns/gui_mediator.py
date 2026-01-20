def main():
    d = DialogueDirector()
    d.create_widgets()
    d.text_field.set_text('')  # OK button disabled
    d.text_field.set_text('Heya')  # enabled
    

class DialogueDirector:
    def __init__(self):
        self.ok_button = None
        self.cancel_button = None
        self.text_field = None

    def create_widgets(self):
        self.ok_button = Button(self, 'OK')
        self.cancel_button = Button(self, 'Cancel')
        self.text_field = TextField(self)

    def widget_changed(self, widget):
        if widget in (self.ok_button, self.text_field):
            if self.text_field.get_text():
                self.ok_button.set_enabled(True)
            else:
                self.ok_button.set_enabled(False)


class Widget:
    def __init__(self, director):
        self.director = director

    def changed(self):
        self.director.widget_changed(self)


class Button(Widget):
    def __init__(self, director, text):
        super().__init__(director)
        self.text = text
        self.enabled = True

    def set_enabled(self, enabled):
        self.enabled = enabled
        print(f'{self.text} button {"en" if enabled else "dis"}abled')


class TextField(Widget):
    def __init__(self, director):
        super().__init__(director)
        self.text = ''

    def set_text(self, text):
        self.text = text
        self.changed()

    def get_text(self):
        return self.text


if __name__ == '__main__':
    main()
