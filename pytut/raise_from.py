def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('b cannot be 0')

    
def divide2(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('b cannot be 0') from e



#divide(3, 0)
#divide2(4, 0)


try:
    divide2(4, 0)
except ValueError as e:
    print('Cause:', e.__cause__)
    print('Exception:', e)


def divide3(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('b cannot be 0') from None


try:
    divide3(10, 0)
except ValueError as e:
    print('Cause:', e.__cause__)
    print('Exception:', e)



