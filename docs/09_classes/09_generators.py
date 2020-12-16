def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


for char in reverse('golf'):
    print(char)
