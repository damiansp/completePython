def is_palindrome(txt):
    clean = txt.lower().replace(' ', '') 
    return clean == clean[::-1]


def find_palindrome(src):
    longest = ''
    for start in range(len(src) - 2):
        for end in range(start + 2, len(src)):
            part = src[start:end]
            if is_palindrome(part) and len(part) > len(longest):
                longest = part
    return longest


def find_all_palindromes():
    return [
        find_palindrome(src) for src in [
            'hellol howow are you?',
            'adcccbdaabcdc',
            'cdcacccccaacbccbbdcabcabdbbb',
            'Sam, was it a cat I saw?',
            'abc' * 100 + 'No lemon no melon' + 'def' * 100]]


if __name__ == '__main__':
    find_all_palindromes()
