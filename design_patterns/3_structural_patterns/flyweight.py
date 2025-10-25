import string


def main():
    ed = TextEditor()
    for char in 'Hello':
        ed.add_character(char, 'Arial', 12)
    ed.add_character('!', 'Arial', 14)
    print(ed.render_text())


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

    def add_character(self, char, font, size):
        style = self.style_factory.get_style(font, size)
        self.characters.append(Character(char, style))

    def render_text(self):
        return ''.join(char.render() for char in self.characters)


class StyleFactory:
    def __init__(self):
        self.styles = {}

    def get_style(self, font, size):
        key = (font, size)
        if key not in self.styles:
            self.styles[key] = CharacterStyle(font, size)
        return self.styles[key]


if __name__ == '__main__':
    main()
