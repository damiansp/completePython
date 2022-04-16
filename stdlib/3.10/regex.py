import re


m = re.search('(?<=abc)def', 'abcdefg')
print(m.group(0))  # def

m = re.search('(?<=-)\w+', 'spam-egg')
print(m.group(0))  # egg

res = re.match(r'pattern', 'string with pattern maybe')  # same as:
prog = re.compile(r'pattern')
res = prog.match('string with pattern maybe')
# but latter more efficint for re-use

txt = 'Words, words,  words, words.'
print(re.split(r'\W+', txt))
print(re.split(r'(\W+)', txt))
print(re.split(r'\W+', txt, maxsplit=1))
print(re.split(r'\n', txt))

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10'))

print(
    re.sub(
        r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
        r'static PyObject*\npy_\1(void)\n{',
        'def my_func():'))


# Regex objects
pattern = re.compile('d')
print(pattern.search('dog'))     # <re.Match object; span=(0, 1), match='d'>
print(pattern.search('dog', 1))  # None

pattern = re.compile('o')
print(pattern.match('dog'))     # None
print(pattern.match('dog', 1))  # <re.Match object; span=(1, 2), match='o'>

pattern = re.compile('o[gh]')
print(pattern.fullmatch('dog'))   # None
print(pattern.fullmatch('ogre'))  # None
print(pattern.fullmatch('doggie', 1, 3))
# <re.Match object; span=(1, 3), match='og'>


m = re.match(r'(\w+) (\w+)', 'Isaac Newton, physicist')
print(m.group(0))
print(m[0])  # same as prev
print(m.group(1))
print(m.group(2))
print(m.group(1, 2))

m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds')
print(f'{m.group("last_name").upper()}, {m.group("first_name")}')

m = re.match(r'(..)+', 'a1b2c3')
print(m.group(1))  # c3


m = re.match(r'(\d+)\.?(\d+)', '24.1632')
print(m.groups())

m = re.match(r'(\d+)\.?(\d+)?', '24')
print(m.groups())  # ('24', None)
print(m.groups('0'))  # ('24', '0')


m = re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)', 'Malcolm Reynolds')
print(m.groupdict())


email = 'tony@tiremove_thisget.net'
m = re.search('remove_this', email)
print(email[:m.start()] + email[m.end():])


# Examples
# Check for a pair
def display_match(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

valid = re.compile(r'^[a2-9tjqk]{5}$')      # possible poker hands
print(display_match(valid.match('akt5q')))  # valid
print(display_match(valid.match('akt5e')))  # invalid
print(display_match(valid.match('akt')))    # invalid
print(display_match(valid.match('727ak')))  # valid

pair = re.compile(r'.*(.).*\1')
print(display_match(pair.match('717ak')))  # pr of 7s
print(display_match(pair.match('718ak')))  # no pairs
print(display_match(pair.match('354aa'))) # pr of aces

