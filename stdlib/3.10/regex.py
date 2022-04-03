import re


m = re.search('(?<=abc)def', 'abcdefg')
print(m.group(0))  # def

m = re.search('(?<=-)\w+', 'spam-egg')
print(m.group(0))  # egg

res = re.match(r'pattern', 'string with pattern maybe')  # same as:
prog = re.compile(r'pattern')
res = prog.match('string with pattern maybe')
# but latter more efficint for re-use




