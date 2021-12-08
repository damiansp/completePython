import numpy as np
import pandas as pd

from printit import printit as p


a = pd.Series([1, 1, 1, np.nan, 1, 1], index=list('abcdef'))
b = pd.Series([0, 1, 2, np.nan, np.nan], index=list('abcde'))
p(a, '\na')
p(b, '\nb')

ageb = a.ge(b)
ageb_fill = a.ge(b, fill_value=0)
p(ageb, '\na >= b')
p(ageb_fill, '\na >=b (filled)')
