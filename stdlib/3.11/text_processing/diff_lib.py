import difflib
import keyword
from pprint import pprint


print(
    difflib.get_close_matches(
        'appel', ['ape', 'apple', 'peach', 'lapel', 'puppy']))
print(difflib.get_close_matches('wheel', keyword.kwlist))
print(difflib.get_close_matches('damian', keyword.kwlist))
print(difflib.get_close_matches('accept', keyword.kwlist))

diff = difflib.ndiff(
    'one\ntwo\nthree\n'.splitlines(keepends=True),
    'ore\nemu\ntree\n'.splitlines(keepends=True))
print(''.join(diff), end='')
diff = difflib.ndiff(
    'one\ntwo\nthree\n'.splitlines(keepends=True),
    'ore\nemu\ntree\n'.splitlines(keepends=True))
diff = list(diff)
print(diff)
print(''.join(difflib.restore(diff, 1)), end='')
print(''.join(difflib.restore(diff, 2)), end='')

s1 = ' abcd'
s2 = 'abcd abcd'
matcher = difflib.SequenceMatcher(None, s1, s2)
print(matcher.find_longest_match(0, len(s1), 0, len(s2)))

# first arg to SeqMatcher is 'isjunk' (e.g., ignore spaces in this ex:)
matcher = difflib.SequenceMatcher(lambda x: x == ' ', s1, s2)
print(matcher.find_longest_match(0, len(s1), 0, len(s2)))


s = difflib.SequenceMatcher(None, 'abxcd', 'abcd')
print(s.get_matching_blocks())

a = 'qabxcd'
b = 'abycdf'
s = difflib.SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print(
        f'{tag:7} a[{i1}:{i2}] --> b[{j1}:{j2}] {a[i1:i2]!r:>8} --> '
        f'{b[j1:j2]!r}')

print(difflib.SequenceMatcher(None, 'tide', 'diet').ratio())
print(difflib.SequenceMatcher(None, 'diet', 'tide').ratio())

s = difflib.SequenceMatcher(
    lambda x: x == ' ',
    'private Thread currentThread;',
    'private volatile Thread currentThread;')
print(round(s.ratio(), 3))
for block in s.get_matching_blocks():
    print('a[%d] and b[%d] match for %d elements' % block)
for opcode in s.get_opcodes():
    print('%6s a[%d:%d] b[%d:%d]' % opcode)


text1 = '''
  1. Beautiful is better than ugly.
  2. Explicit is better than implicit.
  3. Simple is better than complex.
  4. Complex is better than complicated.'''.splitlines(keepends=True)
text2 = '''
  1. Beautiful is better than ugly.
  2. Explicit is better than implicit.
  3. Simple is better than complex.
  4. Flat is better than nested.'''.splitlines(keepends=True)

d = difflib.Differ()
res = list(d.compare(text1, text2))
pprint(res)
