@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octests[1:]).cast(typecode)
    return cls(*memv)
