from unicodedata import name

micro = 'µ'
print(name(micro))     # 'MICRO SIGN'
micro_cf = micro.casefold()
print(name(micro_cf))  # 'GREEK SMALL LETTER MU'
print(micro, micro_cf) # µ μ

es_zett = 'ß'
print(name(es_zett))         # LATIN SMALL LETTER SHARP S
es_zett_cf = es_zett.casefold()
print((es_zett, es_zett_cf)) # 'ß', 'ss'
