import numpy as np


def rpkm(counts, lengths):
    '''Calculate reads per kilobase transcript per million reads
    RPKM = (10^9 * C) / (NL)
    C: No. reads mapped to a gene
    N: Total mapped reads in the experiment
    L: Exon length in base pairs for a gene

    Args:
      counts (array: shape=(n_genes, n_samples)): RNAseq or similar count data
        where columns are individual samples and rows are genes
      lengths (array: shape=(n_genes,)): Gene lengths in base pairs in the same
        order as the rows in counts
    Returns:
      normed (array: shape=(n_genes, n_samples)): the RPKM normalized counts
        matrix.'''
    N = np.sum(counts, axis=0) # colsums = total reads per sample
    L = lengths
    C = counts
    normed = 1e9*C / (N[np.newaxis, :] * L[:, np.newaxis])
    return normed


#       [Cell type A, B]
gene0 = [100, 200]
gene1 = [ 50,   0]
gene2 = [350, 100]
expression_data = [gene0, gene1, gene2]
print(expression_data[2][0]) # 350


# Numpy n-dim arrays
array1d = np.array([1, 2, 3, 4])
print(array1d)       # [1 2 3 4]
print(type(array1d)) # numpy.ndarray
print(array1d.shape) # (4,)

array2d = np.array(expression_data)
print(array2d)       # [[100 200]
                     #  [ 50   0]
                     #  [350 100]]
print(type(array2d)) # numpy.ndarray
print(array2d.shape) # (3, 2)
print(array2d.ndim)  # 2

x = np.array([1, 2, 3], np.int32)
print(x) # [1 2 3]

y = x[:2]
print(y) # [1 2]

y[0] = 6
print(y) # [6 2]
print(x) # [6 2 3]

y = np.copy(x[:2])


# Vectorization
x = np.array([1, 2, 3, 4])
print(x * 2) # [ 2 4 6 8]

y = np.array([0, 1, 2, 1])
print(x + y) # [1 3 5 5]
