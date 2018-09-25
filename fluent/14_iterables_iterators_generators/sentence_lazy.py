import re
import reprlib


WORD_REGEX = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in WORD_REGEX.finditer(self.text):
            yield match.group()
