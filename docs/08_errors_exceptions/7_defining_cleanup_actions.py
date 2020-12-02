'''
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, World!')
'''

def wrong():
    try:
        return True
    finally:
        return False

print(wrong()) # False


def divide(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        print('Answer is infinite')
    else:
        print(f'Answer is {res}')
    finally:
        print('The test is over.')

divide(9, 3) # 3 The test is over
divide(9, 0) # infinite The test is over



