import difflib
import keyword


print(
    difflib.get_close_matches(
        'appel', ['ape', 'apple', 'peach', 'lapel', 'puppy']))
print(difflib.get_close_matches('wheel', keyword.kwlist))
print(difflib.get_close_matches('damian', keyword.kwlist))
print(difflib.get_close_matches('accept', keyword.kwlist))


