from unicodedata import name

signs = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(signs)
