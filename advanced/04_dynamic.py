import math

x = eval('(2 ** 31) - 1')

code = '''
def area_of_sphere(r):
    return 4 * math.pi * r ** 2
'''

context = {}
context['math'] = math
exec(code, context)
#print(context) # a lot of stuff including {'area_of_sphere': <function at ...>}

area_of_sphere = context['area_of_sphere']
print(area_of_sphere(5))




