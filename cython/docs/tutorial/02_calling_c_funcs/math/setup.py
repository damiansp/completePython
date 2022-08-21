from setuptools import Extension, setup

from Cython.Build import cythonize


ext_modules = [Extension('sin', sources=['sin.pyx'], libraries=['m'])]
setup(name='Sin', ext_modules=cythonize(ext_modules))
