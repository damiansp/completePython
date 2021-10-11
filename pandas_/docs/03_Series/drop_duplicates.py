import pandas as pd
from printit import printit


s = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama', 'hippo'],
              name='animal')
s_drop = s.drop_duplicates()
s_last = s.drop_duplicates(keep='last')
s_none = s.drop_duplicates(keep=False)
printit(s, 's')
printit(s_drop, 's_drop')
printit(s_last, 's_last')
printit(s_none, 's_none')
