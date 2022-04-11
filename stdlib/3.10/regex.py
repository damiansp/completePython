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

