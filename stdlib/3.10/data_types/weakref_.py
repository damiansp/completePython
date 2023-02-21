import gc
import weakref


class T(str): pass


d = weakref.WeakKeyDictionary()
k1, k2 = T(), T()
d[k1] = 1  # {k1: 1}
d[k2] = 2  # {k1: 2} [sic], b/c k2 is equal in val to k1
del k1     # {}

# so do this instead
k1, k2 = T(), T()
d = weakref.WeakKeyDictionary()
d[k1] = 1
del d[k1]
d[k2] = 2
del k1


class C:
    def method(self):
        print('Method, man!')


c = C()
r = weakref.ref(c.method)
r()   # 'Method, man!'
r = weakref.WeakMethod(c.method)
r()   # <bound method...>
r()() # 'Method, man!'
del c
gc.collect()
r()   # <None>


class Object:
    pass


o = Object()
r = weakref.ref(o)
o2 = r()
print(o is o2)  # True
del o, o2
print(r())  # None
o = r()
if o is None:
    print('Object deallocated; cannot frobnicate')
else:
    print('Still alive!')


class ExtendedRef(weakref.ref):
    def __init__(self, ob, callback=None, /, **annotations):
        super().__init__(ob, callback)
        self.__counter = 0
        for k, v in annotations.items():
            setattr(self, k, v)

    def __call__(self):
        '''Returns a pair containing the referent and the no. of times the
        reference has been called.
        '''
        ob = super().__call__()
        if ob is not None:
            self.__counter += 1
            ob = (ob, self.__counter)
        return ob
        
