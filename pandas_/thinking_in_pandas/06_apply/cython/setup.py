from   Cython.Build import cythonize
from   distutils.core import setup
import pyximport

pyximport.install(language_level=3)


setup(ext_modules=cythonize('example.pyx'))
