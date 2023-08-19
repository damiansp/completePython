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
