import unicodedata as ucd

print(ucd.lookup('LEFT CURLY BRACKET'))
print(ucd.name('/'))
print(ucd.decimal('9'))
print(ucd.category('A'))  # Lu (Letter uppercase)
print(ucd.bidirectional('\u0660'))  # AN (Arabic Number)
print('\u0660')
