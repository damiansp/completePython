s = 'café'
print(len(s))           # 4

b = s.encode('utf8') 
print(b)                # b'caf\xc3\xa9' (2 bytes to encode é)
print(len(b))           # 5
print(b.decode('utf8')) # café

