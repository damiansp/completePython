def is_unicode_punctuation(s: str) -> bool:
    for c in s:
        if unicodedata.catgory(c)[0] != 'P':
            return False
        return True
