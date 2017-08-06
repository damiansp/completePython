#!/usr/bin/env python3
import cmath # complex math

# Getting Input from User
meaning = input('The meaning of life: ')
print('%s, is it?' %meaning)

x = int(input('x: ')) # 3 only?
y = int(input('y: '))
print('xy = %d' %(x * y))


# cmath and Complex Numbers
print(cmath.sqrt(-1))
print((1 + 3j) * (9 + 4j))

#name = raw_input('What is your name? > ') # 2 only
#print('Why, hello, ' + name, + '!')



# String Representations
print("Hello, world!")
print(repr("Hello, world!"))

#print(str(10000L)) # error in 3
#print(repr(10000L)) # error in 3

temp = 42
print('The temperature is ' + str(temp))
# print('The temperature is ' + `temp`) # 2 only
print('The temperature is ' + repr(temp))
