import sys


'''
while True:
    try:
        x = int(input('Enter a number: '))
        break
    except (NameError, ValueError):
        print('Not a valid Number.')
'''


class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

for name, cls in zip(['A', 'B', 'C'], [A, B, C]):
    print(f'trying {name}...')
    try:
        raise cls()
    except C:
        print('C Exception')
    except B:
        print('B Exception')
    except A:
        print('A Exception')
     

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as e:
    print(f'OS Error: {e}')
except ValueError:
    print('Failed to get int')
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise


try:
    f = open('3_handling_exceptions.py', 'r')
except OSError:
    print('Cannot open file')
else: # if no exception
    print(f'File has {len(f.readlines())} lines')
    f.close()


try:
    raise Exception('spam', 'eggs')
except Exception as e:
    print(type(e)) # <class 'Exception'>
    print(e.args)  # ('spam', 'eggs')
    print(e)       # ('spam', 'eggs')
    x, y = e.args
    print('x:', x) # x: spam
    print('y:', y) # y: eggs


def fail():
    x = 1 / 0

try:
    fail()
except ZeroDivisionError as e:
    print(f'Handling runtimer error: {e}... nooney nooney noo...')
