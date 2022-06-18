import timeit

res = timeit.timeit(
    'palindrome1.find_all_palindromes()', setup='import palindrome1', number=10)
print(res) # ~ 2.562169
