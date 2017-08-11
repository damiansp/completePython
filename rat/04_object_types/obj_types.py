#!/usr/bin/envA python3
import math
import random
import re

print(math.sqrt(math.pi))
print(random.choice([1, 2, 3, 5, 8]))



# Strings------------------------------------------------------------------
B = bytearray(b'spam') # byte/list hybrid
B.extend(b'eggs')
print('B:', B)
print('B.decode():', B.decode())

# String-Specific Methods
s = 'Spam'
print('Location of "pa":', s.find('pa'))
print('Replace:', s.replace('pa', 'lu'))
print('s:', s)
print('upper:', s.upper())
print('isalpha:', s.isalpha())

line = "\n\n     a buncha garbage     \n\n"
print('line:', line)
print('rstrip:', line.rstrip())
print('+lstrip:', line.lstrip().rstrip())

print('formatted: {0}, eggs, and {1}'.format(s, s.upper()))
print('same as: {}, eggs, and {}'.format(s, s.upper()))
print('fancy formatting: {:,.2f}'.format(23434294872394.2384729837))
print('more format options:\n%+.2f | %+05d' %(3.141596, -42))

# Getting Help
print(dir(s))
print(help(s.replace))

# Other ways to code strings
print('ASCII binary value of "\\n":', ord('\n'))
print('a\\x00B\\x00C:', 'a\x00B\x00C')

# Unicode Strings
print('Sp\xc4m') # \xc4 = A with umlaut
print(b'a\x01c') # byte-based string (prints literally)
print('a\x01c')  # Normal byte based string in 2; a^Ac in 3 (\x01 is byte)
print(u'sp\u00c4m') # \u00c4 is also A with umlaut

print('Spam')
print('"Spam".encode("utf-8")', 'Spam'.encode('utf-8'))
print('"Spam".encode("utf-16")', 'Spam'.encode('utf-16'))

# Pattern Matching
match = re.match('Hello[ \t]*(.*)world', 'Hello       Python world')
print(match.group(1))
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:damiansp')
print(match.groups())
print(re.split('[/:]', '/usr/home/fancy/pants'))



# Lists--------------------------------------------------------------------
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(a.pop(1))
print(a)
c = ['d', 'a', 'm', 'i', 'a', 'n']
c.sort()
print(c)
c.reverse()
print(c)

# Generators
G = (letter for letter in c)
print(next(G))
print(next(G))

M = [[-3, -2, -1],
     [ 0,  1,  2],
     [ 3,  4,  5]]

# Map
print(list(map(sum, M)))

print({sum(row) for row in M}) # Set
print({i: sum(M[i]) for i in range(3)})  # Dict




