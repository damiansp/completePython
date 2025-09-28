import string


class CharacterStyle:
    def __init__(self, font, size):
        self.font = font
        self.size = size


class Character:
    def __init__(self, char, style):
        self.char = char
        self.style = style

    def render(self):
        return f'{self.char} ({self.style.font}, {self.style.size})'


class TextEditor:
    def __init__(self):
        self.characters = []
        self.style_factory = StyleFactory()

    def add_characters(self, char, font, size):
        styel = self.style_factory.get_style(font, size)
        self.characters.append(Character(char, style))

    def render_text(self):
        return ''.join(char.render() for char in self.characters)


class StyleFactory:
    def __init__(self):
        self.styles = {}

    def get_style(self, font, size):
        # TODO
        pass
