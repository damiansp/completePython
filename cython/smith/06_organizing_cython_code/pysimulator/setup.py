from distutils.core import setup

from Cython.Build import cythonize


setup(
    name='simulator',
    packages=[
        'simulator', 'simulator.core', 'simulator.utils', 'simulator.plugins'],
    ext_modules=cythonize('**/*.pyx'))
