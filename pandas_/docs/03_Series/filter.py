import pandas as pd

from printit import printit as p


df = pd.DataFrame([[1, 2, 3], [4, 5, 6]],
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
p(df, 'df')

by_name = df.filter(items=['one', 'three'])
p(by_name, 'by_name')

final_e = df.filter(regex='e$', axis=1)
p(final_e, 'final_e')

bbi = df.filter(like='bbi', axis=0)
p(bbi, 'bbi')
