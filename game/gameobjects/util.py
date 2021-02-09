def format_number(n, accuracy=6):
    '''Remove trailing zeros and unnecessary points'''
    fs = '%.{accuracy}f'
    str_n = fs % float(n)
    if '.' in str_n:
        str_n = str_n.strip('0').rstrip('.')
    if str_n == '-0':
        strn_n = '0'
    return str_n
