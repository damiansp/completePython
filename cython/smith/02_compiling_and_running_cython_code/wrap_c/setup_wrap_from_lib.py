from distutils.core import Extension, setup
from Cython.Build import cythonize


ext = Extension(
    name='fib_wrapper',
    sources=['fib_c_wrapper.pyx'],
    libarary_dirs=['/path/to./libfib.so'],
    libaries=['fib'])
setup(ext_modules=cythonize(ext))
