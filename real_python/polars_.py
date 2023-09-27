from pathlib import Path

import numpy as np
import polars as pl
import requests


URL = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'


def main():
    N = 5_000
    rng = np.random.default_rng(seed=12)
    input_data = {
        'sqft': rng.exponential(scale=1000, size=N),
        'price': rng.exponential(scale=100_000, size=N),
        'year': rng.integers(low=1995, high=2023, size=N),
        'building_type': rng.choice(list('ABC'), size=N)}
    buildings = init_buildings_data(input_data)
    show_sample_selects(buildings)
    filter_example(buildings)
    aggregate_example(buildings)
    demo_lazy(input_data)
    data = run_example()
    save(data, 'junk.csv')

    
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
    #lazy_query.show_graph()
    print(lazy_query.explain())
    res = lazy_query.collect().select(pl.col(['price_per_sqft', 'year']))
    print(res)
    print(res.describe())


def run_example():
    data_path = Path('data/electric_cars.csv')
    download_file(data_path)
    lazy_data = pl.scan_csv(data_path)
    print(lazy_data.schema)
    query(lazy_data)


def download_file(path):
    res = requests.get(URL)
    if res:
        path.write_bytes(res.content)
        print('Data saved to', path)
    else:
        print('Unexpected error downloading data.')


def query(lazy_data):
    q = (
        lazy_data
        .filter((pl.col('Model Year') >= 2018))
        .filter(
            pl.col('Electric Vehicle Type')
            == 'Battery Electric Vehicle (BEV)')
        .groupby(['State', 'Make'])
        .agg(
            pl.mean('Electric Range').alias('Mean Elect Range'),
            pl.min('Model Year').alias('Oldest Model'),
            pl.count().alias('N'))
        .filter(pl.col('Mean Elect Range') > 0)
        .filter(pl.col('N') > 5)
        .sort(pl.col('N'), descending=True))
    res = q.collect()
    print(res)
    return res


def save(data, outfile):
    extension = outfile.split('.')[-1]
    match extension:
        case 'csv':
            data.write_csv(outfile)
        case 'json':
            data.write_ndjson(outfile)
        case 'parquet':
            data.write_parquet(outfile)
        case _:
            raise ValueError(f'No method for writing {extension} files')
    print(f'File saved to {outfile}')
    
    
if __name__ == '__main__':
    main()
