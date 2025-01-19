the_string = 'An arbitrary sting of characters like 123.'

the_list = list(the_string)

def add_str(c, string):
    return f'{c}{string}'

for c in the_string:
    print(add_str(c))

res = [add_str(c, '... ') for c in the_string]

res = map(lambda c: add_str(c, '... '), the_str)

