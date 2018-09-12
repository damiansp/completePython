import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text) # abbr if too long


class Foo:
    def __iter__(self):
        pass



# Test
s = Sentence('"The time has come", the Walrus said...')
print(s)

for word in s:
    print(word)

print(list(s))


print(issubclass(Foo, abc.Iterable)) # True
f = Foo()
print(isinstance(f, abc.Iterable))   # True


s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it)        # <iterator object ...>
print(next(it))  # Pig
print(next(it))  # and
print(next(it))  # Pepper
#print(next(it)) # StopIteration

print(list(it))       # []
print(list(iter(s3))) # ['Pig', 'and', 'Pepper']
