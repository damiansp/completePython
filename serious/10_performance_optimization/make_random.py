import pickle

import numpy as np


rand_array = np.random.randn(1_000_000)

with open('random.pkl', 'wb') as f:
    pickle.dump(rand_array, f)
