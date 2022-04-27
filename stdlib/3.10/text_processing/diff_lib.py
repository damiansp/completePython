import difflib
import keyword


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
matcher = diflib.SequenceMatcher(lambda x: x == ' ', s1, s2)
print(matcher.find_longest_match(0, len(s1), 0, len(s2)))

