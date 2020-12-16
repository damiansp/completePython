print(sum(i * i for i in range(10))) # 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x * y for x, y in zip(xvec, yvec))) # 260

def dotprod(xv, yv):
    return sum(x * y for x, y in zip(xv, yv))

print(dotprod(xvec, yvec)) # 260

page = ['how much wood',
        'would a woodchuck chuck',
        'if a woodchuck could chuck wood']
unique_words = set(word for line in page for word in line.split())
print(unique_words)

