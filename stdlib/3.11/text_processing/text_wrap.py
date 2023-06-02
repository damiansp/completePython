import textwrap as tw


print(tw.shorten('Hello, World!', width=13))
print(tw.shorten('Hello, World!', width=12))
print(tw.shorten('Hello, World!', width=10, placeholder='...'))


def test():
    s = '''\
        hello
          world
    '''
    print(repr(s))
    print(repr(tw.dedent(s)))

test()

s = 'hello,\n\nworld!'
print(tw.indent(s, '  '))
print(tw.indent(s, '+ '))
print(tw.indent(s, '+ ', lambda line: True))


wrapper = tw.TextWrapper(initial_indent='* ')  # or
wrapper = tw.TextWrapper()
wrapper.inital_indent = '* '




