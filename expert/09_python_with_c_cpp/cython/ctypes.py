import ctypes
#ctypes.cdll.LoadLibrary('libc.dylib')  # or
from   ctypes.util import find_library
ctypes.cdll.LoadLibrary(find_library('c'))
ctypes.cdll.LoadLibrary(find_library('bz2'))


libc.printf(b'Hello, World!')
