import pandas as pd
from pandas_datareader.data import DataReader


def main():
    symbols = ['AAPL', 'GOOG', 'FB', 'TWTR']
    dfs = []
    for sym in symbols:
        print(f'Fetching data for {sym}...')
        df = DataReader(
            sym, start='2015-01-01', end='2022-10-15', data_source='yahoo')
        df['sym'] = sym
        dfs.append(df)
    stock = pd.concat(dfs)
    print(stock.head())
    print(stock.tail())


if __name__ == '__main__':
    main()
        
            
