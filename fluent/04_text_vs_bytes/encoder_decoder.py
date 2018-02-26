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
      

