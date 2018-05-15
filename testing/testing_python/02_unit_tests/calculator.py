class Calculator():
    def add(self, x, y):
        if type(x) == type(y) == int:
            return x + y
        else:
            raise TypeError('Invalid type {} and {}'.format(type(x), type(y)))


if __name__ == '__main__':
    calc = Calculator()
    res = calc.add(2, 3)
    print(res)
