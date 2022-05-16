from setuptools import Extension, setup


setup(
    name='fibonacci',
    version='1.0',
    description='Computes the nth Fibonacci number',
    ext_modules=[Extension('fibonacci', ['fibonacci.c'])])
