class Calculator():
    def add(self, x, y):
        return x + y


if __name__ == '__main__':
    calc = Calculator()
    res = calc.add(2, 2)
    print(res)
