mylist = [1, 3, -5, 10, -7, 2, 3, -1]
pos = [n for n in my list if n > 0]

vals = ['1', '2', '-3', '-', '4', 'NA', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ints = list(filter(is_int, vals))
