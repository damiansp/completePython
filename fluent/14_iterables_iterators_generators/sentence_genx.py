import re
import reprlib


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')

res1 = [x*3 for x in gen_AB()] # start continue end.
for i in res1:
    print('-->', i)            # --> AAA --> BBB

res2 = (x*3 for x in gen_AB())
println(res2) # <generator object...>
for i in res2:
    print('->', i) # start --> AAA continue --> BBB end.


WORD_REGEX = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in WORD_REGEX.finditer(self.text))
    
