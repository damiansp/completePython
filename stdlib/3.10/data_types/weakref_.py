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


_id2obj_dict = weakref.WeakValueDictionary()


def remember(obj):
    oid = id(obj)
    _id2obj_dict[oid] = obj
    return oid


def id2obj(oid):
    return _id2obj_dict[oid]


kenny = Object()
weakref.finalize(kenny, print, 'You killed Kenny!')
del kenny


def callback(x, y, z):
    print('CALLBACK')
    return x + y + z


obj = Object()
f = weakref.finalize(obj, callback, 1, 2, z=3)
assert f.alive
assert f() == 6  # finalized; callback called
assert not f.alive
f()      # nothing; finalizer dead
del obj  # nothing; finalizer dead

obj = Object()
f = weakref.finalizer(obj, callback, 1, 2, z=3)
f.detach()
new_obj, func, args, kwargs = _
assert not f.alive
assert new_obj is obj
assert func(*args, **kwargs) == 6  # CALLBACK


class TempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()

    def remove(self):
        if self.name is not None:
            shutil.rmtree(self.name)
            self.name = None

    @property
    def removed(self):
        return self.name is None

    def __del__(self):
        self.remove()


class BetterTempDir:
    def __init__(self):
        self.name = tempfile.mkdtemp()
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive
