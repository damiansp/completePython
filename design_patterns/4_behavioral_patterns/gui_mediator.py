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
        pass
