for chunk in pd.read_csv('df.csv', chunksize=500):
    print(chunk.shape)
