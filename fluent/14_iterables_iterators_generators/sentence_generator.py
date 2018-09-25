import re
import reprlib


WORD_PATTERN = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = WORD_PATTERN.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return # optional



def gen_123():
    yield 1
    yield 2
    yield 3

for i in gen_123():
    print(i)

g = gen_123()
for _ in range(3): # 4 throws StopIteration
    print(next(g))


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

for c in gen_AB():
    print('-->', c)
