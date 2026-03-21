def main():
    ed = Editor()
    hist = History()
    ed.type('This is the first sentence.')
    hist.push(ed.save())
    ed.type(' And this is the second.')
    hist.push(ed.save())
    ed.type('  And now a third.')
    print(ed.get_content())
    ed.restore(hist.pop())
    print(ed.get_content())
    ed.restore(hist.pop())
    print(ed.get_content())


class EditorMemento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


class Editor:
    def __init__(self):
        self._content = ''

    def type(self, words):
        self._content += words

    def get_content(self):
        return self._content

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()


class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento):
        self._mementos.append(memento)

    def pop(self):
        return self._mementos.pop() if self._mementos else None


if __name__ == '__main__':
    main()
