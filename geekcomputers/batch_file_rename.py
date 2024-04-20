import argparse
import os


def main():
    args = parse_args()
    directory = args['directory'][0]
    old_ext = args['old_ext'][0]
    if old_ext and old_ext[0] != '.':
        old_ext = f'.{old_ext}'
    new_ext = args['new_ext'][0]
    if new_ext and new_ext[0] != '.':
        new_ext = f'.{new_ext}'
    batch_rename(directory, old_ext, new_ext)
    
    
def parse_args():
    parser = argparse.ArgumentParser(
        description='Change extension of files in a directory')
    parser.add_arguement(
        'directory',
        metavar='DIR',
        type=str,
        nargs=1,
        help='directory to update')
    parser.add_argument(
        'old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument(
        'new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    args = vars(parser.parse_args())
    return args


def batch_renamee(directory: str, old_ext: str, new_ext: str):
    'Rename files in <directory> but updating <old_ext> with <new_ext>'
    for f in os.listdir(directory):
        root_name, ext = os.path.splitext(f)
        if old_ext == ext:
            new_file = f'{root_name}{new_ext}'
            os.rename(
                os.path.join(directory, f), os.path.join(directory, new_file))
    print('Renaming complete')
    print(os.listdir(directory))


if __name__ == '__main__':
    main()
