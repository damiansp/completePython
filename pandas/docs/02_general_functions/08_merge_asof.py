import pandas as pd


left = pd.DataFrame({'a': [1, 5, 10], 'lval': ['a', 'b', 'c']})
right = pd.DataFrame({'a': [1, 2, 3, 6, 7], 'rval': [1, 2, 3, 6, 7]})
madf = pd.merge_asof(left, right, on='a')
madf_noexact = pd.merge_asof(left, right, on='a', allow_exact_matches=False)
madf_forward = pd.merge_asof(left, right, on='a', direction='forward')
madf_nearest = pd.merge_asof(left, right, on='a', direction='nearest')

print(left)
print(right)
print(madf)
print(madf_noexact)
print(madf_forward)
print(madf_nearest)


# indexed dfs:
left = pd.DataFrame({'lval': ['a', 'b', 'c']}, index=[1, 5, 10])
right = pd.DataFrame({'rval': [1, 2, 3, 6, 7]}, index=[1, 2, 3, 6, 7])
madfi = pd.merge_asof(left, right, left_index=True, right_index=True)
print(left)
print(right)
print(madfi)


# Ex:
quotes = pd.DataFrame({
    "time": [pd.Timestamp("2016-05-25 13:30:00.023"),
             pd.Timestamp("2016-05-25 13:30:00.023"),
             pd.Timestamp("2016-05-25 13:30:00.030"),
             pd.Timestamp("2016-05-25 13:30:00.041"),
             pd.Timestamp("2016-05-25 13:30:00.048"),
             pd.Timestamp("2016-05-25 13:30:00.049"),
             pd.Timestamp("2016-05-25 13:30:00.072"),
            pd.Timestamp("2016-05-25 13:30:00.075")],
    "ticker": ["GOOG", "MSFT", "MSFT", "MSFT", "GOOG", "AAPL", "GOOG", "MSFT"],
    "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
    "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]})
trades = pd.DataFrame({
    "time": [pd.Timestamp("2016-05-25 13:30:00.023"),
             pd.Timestamp("2016-05-25 13:30:00.038"),
             pd.Timestamp("2016-05-25 13:30:00.048"),
             pd.Timestamp("2016-05-25 13:30:00.048"),
             pd.Timestamp("2016-05-25 13:30:00.048")],
    "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
    "price": [51.95, 51.95, 720.77, 720.92, 98.0],
    "quantity": [75, 155, 100, 100, 100]})
stock1 = pd.merge_asof(trades, quotes, on='time', by='ticker')
stock2 = pd.merge_asof(
    trades, quotes, on='time', by='ticker', tolerance=pd.Timedelta('2ms'))
stock3 = pd.merge_asof(trades,
                       quotes,
                       on='time',
                       by='ticker',
                       tolerance=pd.Timedelta('2ms'),
                       allow_exact_matches=False)
print(stock1)
print(stock2)
print(stock3)
