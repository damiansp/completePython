from datetime import datetime
from pathlib import Path


HERE = Path.cwd()
HOME = Path.home()
print(HERE)
print(HOME)

python_study_path = Path('/Users/damiansp/Learning/python')
print(python_study_path)

THIS_FILE = Path(__file__)
PARENT_DIR = THIS_FILE.parent
print(THIS_FILE)
print(PARENT_DIR)

# Joining paths
for filepath in Path.cwd().glob('*.txt'):
    new_path = Path('archive') / filepath.name
    #filepath.rename(new_path)


# File system ops with paths
path = Path('~/Learning/python/real_python/test.md')
print(path.name)    # test.md
print(path.stem)    # test
print(path.suffix)  # .md
print(path.anchor)  # (None; Root drive like C:\\ in windows)
print(path.parent)  # ~/Learning/python/real_python


# Reading / Writing
# read shopping_list.md
path = Path.cwd() / 'shopping_list.md'
with path.open(mode='r', encoding='utf-8') as f:
    content = f.read()
    groceries = [line for line in content.splitlines() if line.startswith('*')]
print('\n'.join(groceries))


# alternately
content = path.read_text(encoding='utf-8')
groceries = [line for line in content.splitlines() if line.startswith('*')]
print('\n'.join(groceries))

# or even
content = Path('shopping_list.md').read_text(encoding='utf-8')  # cwd assumed
groceries = [line for line in content.splitlines() if line.startswith('*')]

# write
Path('plain_list.md').write_text('\n'.join(groceries), encoding='utf-8')


# Renaming files
txt_path = Path('hello.txt')
md_path = txt_path.with_suffix('.md')
print(md_path)
#txt_path.replace(md_path)  # writes ./hello.md

md_path = txt_path.with_name('greeting.md')
print(md_path)
#txt_path.replace(md_path)  # writes ./greeting.md


# Copying files
source = Path('shopping_list.md')
dest = source.with_stem('shopping_list_bk')
dest.write_bytes(source.read_bytes())


# Moving/Deleting Files
source = Path('shopping_list_bk.md')
dest = Path('junk.md')
try:
    with dest.open(mode='xb') as f:
        f.write(source.read_bytes())
except FileExistsError:
    print(f'"{dest}" already exists')
else:
    source.unlink()


# Touch
filename = Path('empty.txt')
filename.touch(exist_ok=True)  # overwrites if exists
print(filename.exists())


# Show directory tree
def show_tree(directory):
    print(directory)
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}L {path.name}')


show_tree(Path.cwd()) #.parent)


# Find most recently modified
d = Path.cwd()
time, file_path = max((f.stat().st_mtime, f) for f in d.iterdir())
print(file_path, datetime.fromtimestamp(time))


# Create unique file name
def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path


template = 'test{:03d}.txt'
print(unique_path(Path.cwd(), template))
