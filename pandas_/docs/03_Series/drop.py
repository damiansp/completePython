import numpy as np
import pandas as pd

from printit import printit


s = pd.Series(data=np.arange(3), index=list('ABC'))
printit(s, 's')

sdrop = s.drop(labels=['A', 'C'])
printit(sdrop, 'sdrop')

midx = pd.MultiIndex(
    levels=[['lama', 'cow', 'falcon'], ['speed', 'weight', 'length']],
    codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2,], [0, 1, 2] * 3])
s = pd.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
printit(s, 's')

weightless = s.drop(labels='weight', level=1)
printit(weightless, 'weightless')
