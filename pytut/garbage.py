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

print(count_refs(a_id))     # 2
print(count_refs(b_id))     # 1
print(object_exists(a_id))  # True
print(object_exists(b_id))  # True

a = None
print(count_refs(a_id))     # 1
print(count_refs(b_id))     # 1
print(object_exists(a_id))  # True
print(object_exists(b_id))  # True

gc.collect()
print(object_exists(a_id))  # False
print(object_exists(b_id))  # False
print(count_refs(a_id))     # 0
print(count_refs(b_id))     # 0
