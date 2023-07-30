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

