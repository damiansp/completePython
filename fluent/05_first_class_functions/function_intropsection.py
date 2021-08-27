from inspect import signature


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

print(dir(factorial), '\n')

def upper_case_name(obj):
    return ('%s %s' % (obj.first_name, obj.last_name)).upper()

upper_case_name.short_description = 'Customer name'
print(dir(upper_case_name), '\n')

class C:
    pass

obj = C()

def func():
    pass

print(sorted(set(dir(func)) - set(dir(obj))))
