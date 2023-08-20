walrus = False
print(walrus)
print(walrus := True)
print(walrus)  # True

inputs = []
current = input('Write something: ')
while current != 'quit':
    inputs.append(current)
    current = input('Write something: ')


inputs = []
while True:
    current = input('Write something: ')
    if current == 'quit':
        break
    inputs.append(current)


inputs = []
while (current := input('Write something: ')) != 'quit':
    inputs.append(current)
