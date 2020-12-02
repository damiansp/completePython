#raise NameError('HiThere')
#raise ValueError # = raise ValueError()

try:
    raise NameError('Howdy')
except NameError:
    print('Tossing up an error...')
    #raise

