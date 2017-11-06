import math

code = '''
def area_of_sphere(r):
    return 4 * math.pi * r ** 2
'''

context = {}
context['math'] = math
exec(code, context)

area_of_sphere = context['area_of_sphere']
print(area_of_sphere(1))
