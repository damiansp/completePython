#!/usr/bin/env python3
import math
import random

print(math.sqrt(math.pi))
print(random.choice([1, 2, 3, 5, 8]))

# Strings
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

