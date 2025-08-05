import re


line = 'asdf fjdk; afed, fjek,asdf,      foo'
pattern = re.compile(r'[;,\s]\s*')
print(re.split(pattern, line))
