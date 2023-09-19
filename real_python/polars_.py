import numpy as np
import polars as pl


def main():
    N = 5_000
    rng = np.random.default_rng(seed=12)
    input_data = {
        'sqft': rng.exponential(scale=1000, size=N),
        'year': rng.integers(low=1995, high=2023, size=N),
        'bldg_type': rng.choice(list('ABC'), size=N}}
    buildings = init_buildings_data(data)
    show_sample_selects(buildings)
    filter_example(buildings)
    aggregate_example(buildings)
    demo_lazy(input_data)

    
def init_buildings_data(input_data):
    data = pl.DataFrame(input_data)
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
    

def aggregate_example(buildings):
    print(
        buildings.groupby('building_type').agg([
            pl.mean('sqft').alias('mean_sqft'),
            pl.median('year').alias('median_yr'),
            pl.count()]))


def demo_lazy(input_data):
    buildings_lazy = pl.LazyFrame(input_data)
    print(buildings_lazy)
    lazy_query = (
        buildings_lazy
        .with_columns(
            (pl.col('price') / pl.col('sqft')).alias('price_per_sqft'))
        .filter(pl.col('price_per_sqft') > 100)
        .filter(pl.col('year') < 2010))
    print(lazy_query)
    lazy_query.show_graph()
    print(lazy_query.explain())
    
    
if __name__ == '__main__':
    main()
