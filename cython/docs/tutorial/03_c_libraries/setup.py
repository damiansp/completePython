from setuptools import Extension, setup

from Cython.Build import cythonize


setup(ex_modules=cythonize([Extension('queue', ['queue.pyx'])]))
