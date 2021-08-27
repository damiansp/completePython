symbols = '$¢£¥€'
codes = [ord(symbol) for symbol in symbols]
print(codes)

ASCII_MAX = 127
beyond_ascii = [s for s in symbols if ord(s) > ASCII_MAX]
print(beyond_ascii)

# Cartesian products
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
