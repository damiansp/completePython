import numpy as np


bb = b"These are the times that try men's souls"
mv = memoryview(bb)
print(mv)
print(mv[0], mv[-1])
print(mv[:10])
print(mv[:10][-1])
print(mv.readonly)

ba = bytearray(b"If the facts don't fit the theory, change the facts.")
mutable1 = memoryview(ba)
mutable2 = mutable1[:10]
print(mutable2[0])
#mutable1[0] = 'A'
print(mutable2[0])
print(ba[:10])

np_mv = memoryview(np.ones((10, 20, 30)))
print(np_mv.ndim)
print(np_mv.shape)
print(np_mv.strides)
print(np_mv.format)

dt = np.dtype([('a', np.int8), ('b', np.complex128)])
print(dt)

structured_mv = memoryview(np.empty((10,), dtype=dt))
print(structured_mv.format)
