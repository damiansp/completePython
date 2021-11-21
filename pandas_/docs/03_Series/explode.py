import pandas as pd

from printit import printit


s = pd.Series([[1, 2, 3], 'foo', [], [3, 4]])
printit(s, 's')

sx = s.explode()
printit(sx, 'sx')

sxi = s.explode(ignore_index=True)
printit(sxi, 'sxi')
