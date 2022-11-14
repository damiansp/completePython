import sys

from spectral_norm import spectral_norm


print(f'{spectral_norm(int(sys.argv[1])):.9f}')
