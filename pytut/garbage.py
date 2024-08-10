import ctypes
import gc


def count_refs(addr):
    return ctypes.c_long.from_address(addr).value


def object_exists(obj_id):
    for obj in gc.get_objects():
        if id(obj) == obj_id:
            return True
    return False


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: {hex(id(self))}, B: {hex(id(self.b))}')


class B:
    def __init__(self, a):
        self.a = a
        print(f'A: {hex(id(self.a))}, B: {hex(id(self))}')

        
gc.disable()
a = A()
a_id = id(a)
b_id = id(a.b)

print(count_refs(a_id))
print(count_refs(b_id))
print(object_exists(a_id))
print(object_exists(b_id))
