# 2. Class Objects
class MyClass:
    '''A simple example class'''
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()


class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def __str__(self):
        op = '+' if self.i >= 0 else '-'
        return f'{self.r} {op} {abs(self.i)}i'

x = Complex(3., -4.5)
print(x)
