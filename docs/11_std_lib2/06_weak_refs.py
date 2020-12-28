import gc
import weakref


class A:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


a = A(10) # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a # does NOT create a ref
print(d['primary'])
del a            # remove the one ref
gc.collect()
#print(d['primary']) # no longer exists (throws KeyError)


b = A('ten')
e = {'primary': b}
print(e['primary'])
del b
gc.collect()
print(e['primary']) # still exists
