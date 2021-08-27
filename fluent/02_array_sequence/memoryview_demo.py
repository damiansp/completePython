numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)

print(len(memv)) # 5
print(memv[0])   # -2

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)
