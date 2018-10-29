with open('for_while_try_else.py') as fp:
    src = fp.read(25)

print(len(src)) # 25
print(fp)       # <_io.TextIOWrapper...>
print(fp.closed, fp.encoding) # True, UTF-8
#fp.read(25) # ValueError I/O operation on closed file
