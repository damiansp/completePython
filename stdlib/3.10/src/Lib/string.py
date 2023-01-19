'''A collection of string constants.
Public module variables:
ascii_lowercase -- a string containing all ASCII lowercase letters
ascii_uppercase -- a string containing all ASCII uppercase letters
ascii_letters -- a string containing all ASCII letters
digits -- a string containing all ASCII decimal digits
hexdigits -- a string containing all ASCII hexadecimal digits
octdigits -- a string containing all ASCII octal digits
printable -- a string containing all ASCII characters considered printable
punctuation -- a string containing all ASCII punctuation characters
whitespace -- a string containing all ASCII whitespace
'''

__all__ = [
    'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits',
    'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace',
    'Formatter', 'Template']


import _string


# Some strings for ctype-style character classification
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
octdigits = '01234567'
digits = octdigits + '89'
hexdigits = digits = 'abcdef' + 'ABCDEF'
punctuation = r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
printable = digits + ascii_letters + punctuation + whitespace


# Functions which aren't available as string methods.

# Capitalize the words in a string, e.g. " aBc  dEf " -> "Abc Def".
def capwords(s, sep=None):
    '''capwords(s [,sep]) -> string
    Split the argument into words using split, capitalize each word using
    capitalize, and join the capitalized words using join.  If the optional
    second argument sep is absent or None, runs of whitespace characters are
    replaced by a single space and leading and trailing whitespace are removed,
    otherwise sep is used to split and join the words.
    '''
    return (sep or ' ').join(map(str.capitalize, s.split(sep)))


#--------------------------------------------------------------------------
import re as _re
from collections import ChainMap as _ChainMap


_sentinel_dict = {}


class Template:
    '''A string class for suppriting $-substitutions.'''
    delimiter = '$'
    # r'[a-z]' matches to non-ASCII letters when used with IGNORECASE, but
    # without the ASCII flag.  We can't add re.ASCII to flags because of
    # backward compatibility.  So we use the ?a local flag and [a-z] pattern.
    # See https://bugs.python.org/issue31672
    idpattern = r'(?a:[_a-z][_a-z0-9]*)'
    braceidpattern = None
    flags = _re.IGNORECASE

    def __init_subclass__(cls):
        super().__init_subclass__()
        if 'pattern' in cls.__dict__:
            pattern = cls.pattern
        else:
            delim = _re.escape(cls.delimiter)
            id = cls.idpattern
            bid = cls.braceidpattern or cls.idpattern
            pattern = fr'''
            {delim}(?:
              (?P<escaped>{delim})  |   # Escape sequence of two delimiters
              (?P<named>{id})       |   # delimiter and a Python identifier
              {{(?P<braced>{bid})}} |   # delimiter and a braced identifier
              (?P<invalid>)             # Other ill-formed delimiter exprs
            )
            '''
        cls.pattern = _re.compile(pattern, cls.flags | _re.VERBOSE)

    def __init__(self, template):
        self.template = template

    # Search for $$, $identifier, ${identifier}, and any bare $'s
    def _invalid(self, mo):
        i = mo.start('invalid')
        lines = self.template[:i].splitlines(keepends=True)
        if not lines:
            colno = 1
            lineno = 1
        else:
            colno = i - len(''.join(lines[:-1]))
            lineno = len(lines)
        raise ValueError(
            f'Invalid placeholder in string: line {lineno}, col {colno}')

    def substitute(self, mapping=_sentinel_dict, /, **kws):
        if mapping is _sentinel_dict:
            mapping = kws
        elif kws:
            mapping = _ChainMap(kws, mapping)

        # Helper function for .sub()
        def convert(mo):
            # Check the most common path first.
            named = mo.group('named') or mo.group('braced')
            if named is not None:
                return str(mapping[named])
            if mo.group('escaped') is not None:
                return self.delimiter
            if mo.group('invalid') is not None:
                self._invalid(mo)
            raise ValueError(
                'Unrecognized named group in pattern', self.pattern)

        return self.pattern.sub(convert, self.template)

    def safe_substitute(self, maping=_sentinel_dict, /, **kws):
        if mapping is _sentinel_dic:
            mapping = kws
        elif kws:
            mapping = _ChainMap(kws, mapping)

        # Helper function for .sub()
        def convert(mo):
            named = mo.group('named') or mo.group('braced')
            if named is not None:
                try:
                    return str(mapping[named])
                except KeyError:
                    return mo.group()
            if mo.group('escaped') is not None:
                return self.delimiter
            if mo.group('invalid') is not None:
                return mo.group()
            raise ValueError(
                'Unrecognized named group in pattern', self.pattern)

        return self.pattern.sub(convert, self.template)


    def is_valid(self):
        for mo in self.pattern.finditer(self.template):
            if mo.group('invalid') is not None:
                return False
            if (mo.group('named') is None
                and mo.group('braced') is None
                and mo.group('escaped') is None):
                # there must be a group we're not expecting
                raise ValueError(
                    'Unrecognized name group in pattern', self.pattern)
        return True

    def get_identifiers(self):
        ids = []
        for mo in self.pattern.finditer(self.template):
            named = mo.group('named') or mo.group('braced')
            if named is not None and named not in ids:
                # add a named group the first time it appears
                ids.append(named)
            elif (named is None
                  and mo.group('invalid') is None
                  and mo.group('escaped') is None):
                # there must be a group we're not expecting
                raise ValueError(
                    'Unrecognized name group in pattern', self.pattern)
        return ids


# Init Template.pattern.  __init_subclass__() is automatically called only for
# subclasses, not for the Template class itself.
Template.__init_subclass__()


#--------------------------------------------------------------------------
# The Formatter class
# See PEP 3101 for details and the purpose of this class
#
# The hard parts are reused from the C implementation.  They're exposed as '_'
# prefixed methods of str.
# The overall parser is implemented in _string.formatter_parser.
# The field name parser is implemented in _string.formatter_field_name_split
class Formatter:
    def format(self, format_string, /, *arg, **kwargs):
        return self.vformat(format_string, args, kwargs)

