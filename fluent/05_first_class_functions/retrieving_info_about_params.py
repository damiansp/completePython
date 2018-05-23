import inspect

from positional_to_kw_only_params import tag



def clip(text, max_len=80):
    '''Returns <text> clipped at last space <=  max_len'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None: # No spaces found
        end = len(text)
    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)


sig = inspect.signature(clip)
print('sig:\n', sig)
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

    
sig = inspect.signature(tag)
my_tag = {'name': 'img',
          'title': 'Sunshine Blvd',
          'src': 'sunset.jpg',
          'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print('bound args:\n', bound_args)
for name, val in bound_args.arguments.items():
    print(name, '=', val)

del my_tag['name']
#bound_args = sig.bind(**my_tag) # now throws TypeError


