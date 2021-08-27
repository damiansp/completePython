class LoadSave:
    def __init__(self, filename, *attribute_names):
        self.filename = filename
        self.__attribute_names = []
        for name in attribute_names:
            if name.startswith('__'):
                name = f'_{self.__class__.__name__}{name}'
            self.__attribute_names.append(name)

    def save(self):
        with open(self.filename, 'wb') as fh:
            data = []
            for name in self.__attribute_names:
                data.append(getattr(self, name))
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open(self.filename, 'rb') as fh:
            data = pickle.load(fh)
            for name, value in zip(self.__attribute_names, data):
                setattr(self, name, value)


class FileStack(Undo, LoadSave):
    def __init__(self, filename):
        Undo.__init__(self)
        LoadSave.__init__(self, filename, '__stack')
        self.__stack = []

    def load(self):
        super().load()
        self.clear()
