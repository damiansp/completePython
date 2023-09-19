import os
from pathlib import Path, PurePath, PurePosixPath


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
