import pandas as pd

from printit import printit


animals = pd.Series(['llama', 'cow', 'llama', 'beetle', 'llama'])
dup = animals.duplicated()
printit(dup, 'dup')

last_dup = animals.duplicated(keep='last')
printit(last_dup, 'last_dup')

no_dup = animals.duplicated(keep=False)
print(no_dup, 'no_dup')

