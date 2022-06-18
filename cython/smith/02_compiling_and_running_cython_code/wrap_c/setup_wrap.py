from distutils.core import Extension, setup
from Cython.Build import cythonize


ext = Extension(name='fib_wrapper', sources=['fib.c', 'fib_c_wrapper.pyx'])
setup(ext_modules=cythonize(ext))
