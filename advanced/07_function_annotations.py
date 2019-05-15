#import Util

#Util.is_unicode_punctuation('zebr\a')
#Util.is_unicode_punctuation(s='!@#?')
#Util.is_unicode_punctuation(('!', '@'))


def is_unicode_punctuation(s: str) -> bool:
    for c in s:
        if unicodedata.category(c)[0] != 'P':
            return False
    return True

print(is_unicode_punctuation('zebr\a'))   # F
print(is_unicode_punctuation(s='!@#?'))   # T
print(is_unicode_punctuation(('!', '@'))) # T


# Type-checking decorator
def strictly_typed(function):
    annotations = function.__annotations__
    arg_spec = inspect.getfullargspec(function)
    assert 'return' in annotations, 'missing type for return value'
    for arg in arg_spec.args + arg_spec.kwonlyargs:
        assert arg in annotations, ('missing type parameter "' + arg + '"')

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        for name, arg in ((list(zip(arg_spec.args, args))
                           + list(kwargs.items()))):
            assert isinstance(arg, annotations[name]), \
                ('expected argument "{0}" of {1} got {2}'.format(
                    name, annotations[name], type(arg)))
        result = function(*args, **kwargs)
        assert isinstance(result, annotations['return']), \
            ('expected return of {0} got {1}'.format(
                annotations['return'], type(result)))
        return result

    return wrapper



@strictly_typed
def is_unicode_punctuation2(s: str) -> bool:
    for c in s:
        if unicodedata.category(c)[0] != 'P':
            return False
    return True

print(is_unicode_punctuation2('zebr\a'))   # F
print(is_unicode_punctuation2(s='!@#?'))   # T
print(is_unicode_punctuation2(('!', '@'))) # AssertionError

    
# range() updated to return floats
def range_of_floats(*args) -> "author=Reginald Perrin":
    return (float(x) for x in range(*args))


print(list(range_of_floats(3, 10)))
            












