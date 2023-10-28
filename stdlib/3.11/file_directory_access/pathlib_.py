import os
from pathlib import Path, PosixPath, PurePath, PurePosixPath


# Basic usage
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])
print(list(p.glob('**/*.py')))

etc = Path('/etc')
q = etc / 'init.d' / 'reboot'
print(q)
print(q.resolve())
print(q.exists())
print(q.is_dir())

if q.exists():
    with q.open() as f:
        print(f.readline())


# Pure Paths: path-handling ops that don't actually access filesystems
print(PurePath('setup.py'))
print(PurePath('foo', 'some/path', 'bar'))
print(PurePath(Path('foo'), Path('bar')))
print(PurePath())                         # '.'
print(PurePath('/etc', '/usr', 'lib64'))  # '/usr/lib64'
print(PurePath('foo//bar'))
print(PurePath('//foo/bar'))              # //foo/bar
print(PurePath('foo/./bar'))              # foo/bar
print(PurePath('foo/../bar'))             # foo/../bar != bar if foo is symlink


print(PurePosixPath('/etc'))
print(PurePosixPath('foo') == PurePosixPath('FOO'))  # False
print(PurePosixPath('FOO') in {PurePosixPath('foo')})  # True


# Operators ('/')
p = PurePath('/etc')
print(p)
print(p / 'init.d' / 'apache2')
q = PurePath('bin')
print('/usr' / q)
print(p / '/abs_path')  # /abs_path

print(os.fspath(p))  # /etc
print(str(p))        # '/etc'
print(bytes(p))      # b'/etc'


# Path parts
p = PurePath('/usr/bin/python3')
print(p.parts)  # / usr bin python3


# Methods/Properties
print(PurePosixPath('/etc').root)    # /
print(PurePosixPath('/etc').anchor)  # /

p = PurePosixPath('/foo/bar/setup.py')
print(p.parents[0])  # /foo/bar
print(p.parents[1])  # /foo
print(p.parents[2])  # /

p = PurePosixPath('/a/b/c/d')
print(p.parent)  # '/a/b/c'
root = PurePosixPath('/')
print(root.parent)  # /
here = PurePosixPath('.')
print(here.parent)  # .
p = PurePosixPath('foo/..')
print(p.parent)     # foo (!)
#print(p.resolve().parent())  # to get expected behavior

p = PurePosixPath('my/library/setup.py')
print(p.name)    # setup.py
print(p.suffix)  # .py
print(p.stem)    # setup

c = PurePosixPath('my/library/lib.tar.gz')
print(c.name)      # lib.tar.gz
print(c.suffix)    # .gz
print(c.suffixes)  # ['.tar', '.gz']
print(c.stem)      # /lib.tar

p = PurePosixPath('/etc/passwd')
print(p.as_uri())  # file:///etc/passwd

print(PurePosixPath('/a/b').is_absolute())  # True
print(PurePosixPath('a/b').is_absolute())   # False

print(p.is_relative_to('/etc'))  # True
print(p.is_relative_to('/usr'))  # False

print(PurePosixPath('/etc').joinpath('passwd'))
print(PurePosixPath('/etc').joinpath(PurePosixPath('passwd')))
print(PurePosixPath('/etc').joinpath('passwd', 'apache2'))

print(PurePath('a/b.py').match('*.py'))      # True
print(PurePath('a/b/c.py').match('b/*.py'))  # True
print(PurePath('a/b/c.py').match('a/*.py'))  # False
print(PurePath('/a.py').match('/*.py'))      # True
print(PurePath('a/b.py').match('/*.py'))     # False
print(PurePosixPath('b.py').match('*.PY'))   # False
#print(PureWindowsPath('b.py').match('*.PY'))# True

print(p.relative_to('/'))      # etc/passwd
print(p.relative_to('/etc'))   # passwd
#print(p.relative_to('/usr'))  # ValueError: not a subpath


# Concrete Paths
print(Path('setup.py'))
print(PosixPath('/etc'))
print(os.name)  # posix

# Methods
print('CWD:', Path.cwd())
print('Home:', Path.home())
p = Path('./pathlib_.py')
print('stats:')
print('size:', p.stat().st_size)
print('time:', p.stat().st_mtime)
print('chmod:', p.stat().st_mode)
#p.chmod(0o444)

print('exists:', p.exists())
print('./foo?', Path('./foo').exists())

p = PosixPath('~/repos/python')
print(p.expanduser())
p = Path('.').parent
print(sorted(p.glob('*.py')))
print(sorted(p.glob('**/*.py')))  # **: this dir and all subdirs


p = Path('/Users/damiansp/Learning/python/stdlib/3.11')
for child in p.iterdir():
    print(child)


for root, dirs, files in p.walk(on_error=print):
    print(
        root,
        'consumes',
        sum((root / f).stat().st_size for f in files),
        'bytes in',
        len(files),
        'non-directory files')
    if '__pycache__' in dirs:
        dirs.remove('__pycache__')


# Use w caution! Deletes everything reachable from <top>
#for root, dirs, files in top.walk(top_down=False):
#    for name in files:
#        (root / name).unlink()
#    for name in dirs:
#        (root / name).rmdir()


p = Path('.')
with p.open() as f:
    print(f.readlines())

p = Path('./my_binary')
n = p.write_bytes(b'binary file contents')
print(n)  # n bytes
print(p.read_bytes())

p = Path('./plaintext.txt')
n = p.write_text('Just some plain text')
print(n)  # n chars
print(p.read_text())

