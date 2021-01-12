# old way
class MyBaseClass:
    def __init__(self, val):
        self.val = val


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


# but...
class TimesTwo:
    def __init__(self):
        self.val *= 2


class PlusFive:
    def __init__(self):
        self.val += 5

        
class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, val):
        MyBaseClass.__init__(self, val)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

        
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, val):
        MyBaseClass.__init__(self, val)
        TimesTwo.__init__(self) # Doh! need to reorder!
        PlusFive.__init__(self)


foo = OneWay(5)
bar = AnotherWay(5)
print(f'First ordering; val = 5*2 + 5 = {foo.val}')
print(f'Second ordering; expected 2 * (5 + 5), but is: {bar.val}')


class TimesSeven(MyBaseClass):
    def __init__(self, val):
        MyBaseClass.__init__(self, val)
        self.val *= 7

        
class PlusNine(MyBaseClass):
    def __init__(self, val):
        MyBaseClass.__init__(self, val)
        self.val += 9


class ThisWay(TimesSeven, PlusNine):
    def __init__(self, val):
        TimesSeven.__init__(self, val)
        PlusNine.__init__(self, val) # passes in val from init (resets)

        
foo = ThisWay(5)
print(f'Expected 5*7 + 9 = 44, but got: {foo.val}') # 14
