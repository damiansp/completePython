import weakref


class T(str): pass


d = weakref.WeakKeyDictionary()
k1, k2 = T(), T()
d[k1] = 1  # {k1: 1}
d[k2] = 2  # {k1: 2} [sic], b/c k2 is equal in val to k1
del k1     # {}

# so do this instead
d[k1] = 1
del d[k1]
d[k2] = 2
del k1
