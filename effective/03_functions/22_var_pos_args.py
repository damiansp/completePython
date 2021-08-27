def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('My numbers are', [1, 2])
log('Hi there', [])


def log2(msg, *vals):
    if not vals:
        print(msg)
    else:
        val_str = ', '.join(str(x) for x in vals)
        print(f'{msg}: {val_str}')

log2('My numbers are', 1, 2)
log2('Hi there')


