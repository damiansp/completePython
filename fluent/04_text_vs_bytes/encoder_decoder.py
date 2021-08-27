import locale
import os
import sys


for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

city = 'São Paolo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
#print(city.encode('cp437')) # UnicodeEncodeError
print(city.encode('cp437', errors='ignore'))            # So Paolo
print(city.encode('cp437', errors='replace'))           # S?o Paolo
print(city.encode('cp437', errors='xmlcharrefreplace')) # S&#227;o Paolo

# Decode error handling
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))    # Montréal
print(octets.decode('iso8859_7')) # Montrιal
print(octets.decode('koi8_r'))    # MontrИal
#print(octets.decode('utf_8'))    # UnicodeDecodeError
print(octets.decode('utf_8', errors='replace')) # Montr�al
      

u16 = 'El Niño'.encode('utf_16')
print(u16) # b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
           # The first to bytes \xff\xfe denote little-endian byte-order
print(list(u16))
# [255, 254, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]

u16le = 'El Niño'.encode('utf_16le') # le: little-endian
print(list(u16le))
#           [69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]
u16be = 'El Niño'.encode('utf_16be') # be: big-endian                       
print(list(u16be))
#           [0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111]


open('cafe.txt', 'w', encoding='utf_8').write('café')
print(open('cafe.txt').read()) # Bad: encoding not given. Works on this machine,
                               # but is system-encoding dependent
# Fixing the bug:
fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp) # <_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf_8'>
print(fp.write('café'))            # 4
fp.close()

print(os.stat('cafe.txt').st_size) # 5
fp2 = open('cafe.txt')
print(fp2) # <_io.TextIOWrapper name='cafe.txt' mode='r' encoding='UTF-8'>
print(fp2.encoding)                # UTF-8
print(fp2.read())                  # café

fp3 = open('cafe.txt', encoding='utf_8')
print(fp3) # <_io.TextIOWrapper name='cafe.txt' mode='r' encoding='utf_8'>
print(fp3.read())                  # café

fp4 = open('cafe.txt', 'rb')
print(fp4) # <_io.BufferedReader name='cafe.txt'>
print(fp4.read())                  # b'caf\xc3\xa9'



expressions = [
    'locale.getpreferredencoding()', 'type(my_file)', 'my_file.encoding',
    'sys.stdout.isatty()', 'sys.stdout.encoding', 'sys.stdin.isatty()',
    'sys.stdin.encoding', 'sys.stderr.isatty()', 'sys.stderr.encoding',
    'sys.getdefaultencoding()', 'sys.getfilesystemencoding()']
my_file = open('dummy', 'w')

for e in expressions:
    value = eval(e)
    print(e.rjust(30), '=>', repr(value))
