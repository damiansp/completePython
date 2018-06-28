charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))

imposter = {
    'name': 'Charles L. Dodgson', 'born': 1832}
print(imposter, charles)
print(imposter == charles) # True
print(imposter is charles) # False
print(id(imposter))

lewis['psuedonym'] = 'Lewis Carroll'
print(charles)



# Tuples and "immutability"
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2) # True
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2) # False
