def tag(name, *content, cls=None, **attributes):
    '''Genearate one or more HTML tags'''
    if cls is not None:
        attributes['class'] = cls
    if attributes:
        attribute_str = ''.join(' %s="%s"' % (attr, value)
                                for attr, value in sorted(attributes.items()))
    else:
        attribute_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attribute_str, c, name)
                         for c in content)
    else:
        return '<%s%s />' % (name, attribute_str)


# Test
print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))

my_tag = {'name': 'img',
          'title': 'Sunset Blvd',
          'src': 'sunset.jpg',
          'cls': 'framed'}
print(tag(**my_tag))


def f(a, *, b): # forces b to be keyword-only arg
    return a * b

print(f(1, b=2))
#f(1, 2) # throws TypeError


          
