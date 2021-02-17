from sys import getrefcount


print('--- Before Assignment ---')
print(f'Ref to val_1: {getrefcount("val_1")}')
print(f'Ref to val_2: {getrefcount("val_2")}')
x = 'val_1'

print('\n--- After Assignment ---')
print(f'Ref to val_1: {getrefcount("val_1")}')
print(f'Ref to val_2: {getrefcount("val_2")}')
x = 'val_2'

print('\n--- After Reassignment ---')
print(f'Ref to val_1: {getrefcount("val_1")}')
print(f'Ref to val_2: {getrefcount("val_2")}')


def show_locals(arg=None):
    my_local = True
    print(locals())


def show_refcount(arg):
    return getrefcount(arg)

show_locals() # {'arg': None, 'my_local': True}
print(getrefcount('val_3'))   # 3
print(show_refcount('val_3')) # 5
