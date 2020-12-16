import re

s = 'which foot or hand fell fastest'
print(re.findall(r'\bf[a-z]*', s))

s2 = 'the cat in in the the hat'
print(re.sub(r'(\b[a-z]+) \1', r'\1', s2))

print(('tea for too').replace('oo', 'wo'))
