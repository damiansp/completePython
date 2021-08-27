from setuptools import setup

setup(name='hello_opencv',
      version='0.1.0',
      py_modules = ['hello_opencv'],
      license='MIT',
      description='An example python opencv project',
      long_description=open('README.md').read(),
      isntall_requires=['numpy', 'opencv-python'],
      url='https://github.com/albertofernandez',
      author='Alberto Fernandez',
      author_email='fernandezvillan.alberto@gmail.com')
