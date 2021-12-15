TEST = True


def cache(filename, **decorator_kwargs):
    if TEST:
        def get_cached():
            data = pd.read_csv(filename)
            print('Retrieved cached data')
            if 'index' not in decorator_kwargs or decorator_kwargs['index']:
                data.index = data['Unnamed: 0']
                data.drop('Unnamed: 0', axis=1, inplace=True)
                data.index.name = None
            return data
        
        def inner(f):
            def test_wrapper(*args, **kwargs):
                try:
                    out = get_cached()
                except FileNotFoundError:
                    print('No cached data. Generating...')
                    out = f(*args, **kwargs)
                    out.to_csv(filename, **decorator_kwargs)
                return out
            return test_wrapper
        return inner

    else:
        def wrapper(f, *args, **kwargs):
            f(*args, **kwargs)

        return wrapper


if __name__ == '__main__':
    import os
    
    import numpy as np
    import pandas as pd

    @cache(filename='/tmp/random_df.csv', index=False)
    def create_df(nrow, ncol):
        data = np.random.rand(nrow, ncol)
        columns = list('abcdefghijklmnopqrstuvwxyz')[:ncol]
        df = pd.DataFrame(data, columns=columns)
        return df

    @cache(filename='/tmp/polys.csv')
    def get_polys(x, max_poly=4):
        df = pd.DataFrame(index=x)
        for exp in range(2, max_poly + 1):
            df[f'x^{exp}'] = x ** exp
        return df

    rand_5x5 = create_df(5, 5)
    x = np.array([1, 1.1, 2, 2.1, 2.2, 3])
    polys = get_polys(x)

    print('/tmp/:', os.listdir('/tmp/'))
    cached_polys = get_polys(x)
    print(cached_polys)
