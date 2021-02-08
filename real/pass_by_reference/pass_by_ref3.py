def main():
    counter = 0
    print(greet('Alice', counter))
    print('Counter:', counter)   # 0
    print(greet('Bob', counter))
    print('Counter:', counter)   # 0

    greeting, counter = greet2('Alice', counter)
    print(f'{greeting} (counter: {counter})')  # 1
    greeting, counter = greet2('Bob', counter)
    print(f'{greeting} (counter: {counter})')  # 2
    

def greet(name, counter):
    counter += 1
    return f'Hi, {name}!'


def greet2(name, counter):
    return f'Hi, {name}', counter + 1


main()
