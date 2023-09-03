import numpy as np
import polars as pl


def main():
    buildings = init_buildings_data()
    show_sample_selects(buildings)
    filter_example(buildings)
    

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


def show_sample_selects(buildings):
    print(buildings.select('sqft'))
    print(buildings.select(pl.col('sqft')))
    print(buildings.select(pl.col('sqft').sort() / 1000))


def filter_example(buildings):
    after_2015 = buildings.filter(pl.col('year') > 2015)
    print(after_2015.shape)
    print(after_2015.select(pl.col('year').min()))
    

if __name__ == '__main__':
    main()
