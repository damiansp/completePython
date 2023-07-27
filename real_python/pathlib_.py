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
