import random
import re
from typing import NamedTuple


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


# search() v. match()
print(re.match('c', 'abcdef'))  # None: match checks beginning of str only
print(re.search('c', 'abcdef')) # Match

print(re.match('X', 'A\nB\nX', re.MULTILINE))  # None; first line only
print(re.search('^X', 'A\nB\nX', re.MULTILINE)) # match (^ required)


# Phonebook
text = '''Bob Dobolina: 213.456.7890 123 Some St

Justin Case: 314.567.8901 44 Safety Lane


Seymour Butts: 405.678.9012 88 Bleacher Blvd'''
entries = re.split('\n+', text)
print('Entries:', entries)

print([re.split(':? ', entry, 3) for entry in entries])
print([re.split(':? ', entry, 4) for entry in entries])


def repl(m):
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + ''.join(inner_word) + m.group(3)

text = 'Satan oscillate my metallic sonatas'
print(re.sub(r'(\w)(\w+)(\w)', repl, text))
print(re.sub(r'(\w)(\w+)(\w)', repl, text))

text = 'He was carefully disguised, but the police caught him quickly.'
print('advs:', re.findall(r'\w+ly\b', text))

for m in re.finditer(r'\w+ly\b', text):
    print(f'{m.start():02d}-{m.end():02d}: {m.group(0)}')


# Raw string notation (r-strings):
print(r'\W(.)\1\W' == '\\W(.)\\1\\W')  # True


class Token(NamedTuple):
    ttype: str
    value: str
    line: int
    column: int


def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    tokens = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Int of decimal no.
        ('ASSIGN',   r':='),           # Assignment op
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arith. operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.')]            # Any other char
    token_regex = '|'.join(f'(?P<{name}>{re})' for (name, re) in tokens)
    line = 1
    line_start = 0
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        col = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = 'KEYWORD'
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line}')
        yield Token(kind, value, line, col)


statements = '''
    IF quantity THEN
        total := total + price*quantity;
        tax := price * 0.05;
    ENDIF;'''

for token in tokenize(statements):
    print(token)
