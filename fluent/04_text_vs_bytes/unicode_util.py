import string
from unicodedata import combining, normalize


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold()
            == normalize('NFC', str2).casefold())


def remove_diacritics(text):
    norm_text = normalize('NFD', text)
    shaved = ''.join(c for c in norm_text if not combining(c))
    return normalize('NFC', shaved)


order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
print(remove_diacritics(order))
Greek = 'Ζέφυρος, Zéfiros'
print(remove_diacritics(Greek))


def shave_marks_latin(text):
    '''Remove all diacritics from Latin base characters'''
    norm_text = normalize('NFD', text)
    latin_base = False
    keepers = []
    for c in norm_text:
        if combining(c) and latin_base:
            continue # ignore diacritc on Latin base char
        keepers.append(c)
        # if not cominining char, new base char
        if not combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return normalize('NFC', shaved)

print(shave_marks_latin(order))
print(shave_marks_latin(Greek))
