from unicodedata import normalize, name

s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2)) # 4, 5
print(s1 == s2)         # False

s1_nfc = normalize('NFC', s1)
s2_nfc = normalize('NFC', s2)
s1_nfd = normalize('NFD', s1)
s2_nfd = normalize('NFD', s2)
print(len(s1_nfc), len(s2_nfc)) # 4, 4
print(len(s1_nfd), len(s2_nfd)) # 5, 5
print(s1_nfc == s2_nfc)         # True
print(s1_nfd == s2_nfd)         # True

ohm = '\u2126'
print(name(ohm))       # 'OHM SIGN'
ohm_norm = normalize('NFC', ohm)
print(name(ohm_norm))  # 'GREEK CAPITAL LETTER OMEGA'
print(ohm == ohm_norm) # False

micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print((name(micro), name(micro_kc)))
