from pathlib import Path


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


# Pure Paths
