from os import makedirs
from os.path import exists, pardir


def create_dir(name):
    dirname = f'{pardir}/{name}'
    if exists(dirname):
        print('Folder exists. Not overwriting.')
    else:
        makedirs(dirname)

