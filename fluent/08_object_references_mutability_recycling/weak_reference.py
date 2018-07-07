import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)   # <weakref at...'; to set at ...>
print(wref()) # {0, 1}

a_set = {2, 3, 4}
print(wref()) # None
print(wref() is None) # True

