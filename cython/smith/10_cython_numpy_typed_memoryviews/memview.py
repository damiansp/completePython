bb = b"These are the times that try men's souls"
mv = memoryview(bb)
print(mv)
print(mv[0], mv[-1])
print(mv[:10])
print(mv[:10][-1])
