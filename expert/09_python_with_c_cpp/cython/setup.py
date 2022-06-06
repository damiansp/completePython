from setuptools import Extension, setup
import os

try:
    USE_CYTHON = bool(os.environ.get('USE_CYTHON'))
    import Cython
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension('fibonacci', [f'fibonacci{ext}'])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)


setup(
    name='fibonacci',
    ext_modules=extension,
    extras_require={'with-cython': ['cython==0.29.30']})
