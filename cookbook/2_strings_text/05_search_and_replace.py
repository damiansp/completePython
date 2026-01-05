from calendar import month_abbr
import re


text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yup'))  # replaces all

text = 'Today is 11/27/2012. PyCon starts on 3/13/2013'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
#       Today is 2012-11-27. PyCon starts on 2013-3-13


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return f'{m.group(2)} {mon_name} {m.group(3)}'

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(change_date, text))
# Today is 27 Nov 2012. PyCon starts on 13 Mar 2013


# find no. of substitutions
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)  # Today is 2012-11-27. PyCon starts on 2013-3-13
print(n)        # 2
