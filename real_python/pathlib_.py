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
    filepath.rename(new_path)


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
