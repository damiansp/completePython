import numpy as np
import pandas as pd

print(pd.get_option('display.max_rows'))  # 60
pd.set_option('display.max_rows', 120)
pd.reset_option('display.max_rows')


# options of note:
# - max_columns
# - chop_threshold (float vals below thresh display as 0)
# - colheader_justify
# - date_dayfirst (T/F)
# - date_yearfirst (T/F)
# - precision (float displays)

s = pd.Series(np.random.randn(5))
pd.set_eng_float_format(accuracy=3, use_eng_prefix=False)
print(s)

pd.set_eng_float_format(accuracy=3, use_eng_prefix=True)
print(s)
