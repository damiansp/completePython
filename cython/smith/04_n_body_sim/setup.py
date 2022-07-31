from distutils.core import setup

from Cython.Build import cythonize


setup(name='n_body', ext_modules=cythonize('n_body.pyx'))
