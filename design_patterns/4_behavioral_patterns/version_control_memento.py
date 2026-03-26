import time


class Commit:
    def __init__(self, content):
        self._content = content
        self._timestamp = time.time()

    def get_content(self):
        return self._content

    def get_timestamp(self):
        return self._timestamp


class File:
    def __init__(self, name):
        self._name = name
        self._content = ''

    def write(self, content):
        pass 
