mt = {'n': 4}


def square(n_dict):
    n_dict['n'] *= n_dict['n']


square(mt)
print(mt) # {'n': 16}


