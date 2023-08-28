import numpy as np
import polars as pl


def main():
    buildings = init_buildings_data()



def init_buildings_data():
    N = 5_000
    rng = np.random.default_rng(seed=12)
    data = pl.DataFrame({
        'sqft': rng.exponential(scale=1000, size=N),
        'year': rng.integers(low=1995, high=2023, size=N),
        'bldg_type': rng.choice(list('ABC'), size=N)})
    print(data.head())
    print('schema:', data.schema)
    print(data.describe())
    return data


if __name__ == '__main__':
    main()
