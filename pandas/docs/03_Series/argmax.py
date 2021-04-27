import pandas as pd


s = pd.Series({'Corn Flakes': 100.,
               'Almond Delight': 110.,
               'Cinnamon Toast Crunch': 120.,
               'Cocoa Puffs': 110.})
print(f's:\n{s}')
print(f's.argmin(): {s.argmin()}')
print(f's.argmax(): {s.argmax()}')
