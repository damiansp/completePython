import os.path
from string import Template
import time


t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='bandit fund'))

t = Template('Return the $item to $owner.')
d = dict(item='plow', owner='peasant')
print(t.substitute(d))

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print(f'{filename} -> {newname}')
