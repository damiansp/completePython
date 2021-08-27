from   collections import defaultdict
import itertools as it

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from   scipy import stats

#plt.style.use('style/elegant.mplstyle') 


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


# Broadcasting
x = np.array([1, 2, 3, 4])
x = np.reshape(x, (len(x), 1))
print(x) # [[1] [2] [3] [4]]

y = np.array([0, 1, 2, 1])
y = np.reshape(y, (1, len(y)))
print(y) # [[0 1 2 1]]

print(x.shape) # (4, 1)
print(y.shape) # (1, 4)

outer = x * y
print(outer) # [[0 1 2 1]
             #  [0 2 4 2]
             #  [0 3 6 3]
             #  [0 4 8 4]]
print(outer.shape) # (4, 4)


# Pandas
with open('../data/counts.txt', 'rt') as f:
    data_table = pd.read_csv(f, index_col=0)

print(data_table.head())

samples = list(data_table.columns)

with open('../data/genes.csv', 'rt') as f:
    gene_info = pd.read_csv(f, index_col=0)
print(gene_info.head())

print('Genes in data_table:', data_table.shape[0])
print('Genes in gene_info:', gene_info.shape[0])

matched_index = pd.Index.intersection(data_table.index, gene_info.index)
counts = np.asarray(data_table.loc[matched_index], dtype=int)
gene_names = np.array(matched_index)
print(f'{counts.shape[0]} genes measured in {counts.shape[1]} individuals')

gene_lengths = np.asarray(gene_info.loc[matched_index]['GeneLength'], dtype=int)
print(counts.shape)       # 20500, 375
print(gene_lengths.shape) # 20500


# Normalization
total_counts = np.sum(counts, axis=0) # colsums
density = stats.kde.gaussian_kde(total_counts)
x = np.arange(min(total_counts), max(total_counts), 1000)

fig, ax = plt.subplots()
ax.plot(x, density(x))
ax.set_xlabel('Total counts per individual')
ax.set_ylabel('Density')
plt.show()
print(f'Count statistics:\n  min:  {np.min(total_counts):.4f}\n'
      f'  mean: {np.mean(total_counts):.4f}\n'
      f'  max:  {np.max(total_counts):.4f}')


# Normalizing library sizes between samples
np.random.seed(seed=14)
samples_index = np.random.choice(range(counts.shape[1]), size=70, replace=False)
counts_subset = counts[:, samples_index]


def reduce_xaxis_labels(ax, factor):
    '''Show only every ith label to prevent crowding on the x-axis; e.g., 
      factor = 2 would plot every 2nd x-axis label, starting at the first.
    Args:
      ax (matplotlib plot axis): the axis to adjust
      factor (int): factor to reduce the number of x-axis labels by
    '''
    plt.setp(ax.xaxis.get_ticklabels(), visible=False)
    for label in ax.xaxis.get_ticklabels()[factor - 1::factor]:
        label.set_visible(True)


# Barplot of expression counts by individual
fig, ax = plt.subplots(figsize=(4.8, 2.4))
#with plt.style.context('style/thinner.mplstyle'): # notebook usage
ax.boxplot(counts_subset)
ax.set_xlabel('Individuals')
ax.set_ylabel('Gene expression counts')
reduce_xaxis_labels(ax, 5)
plt.show()

fig, ax = plt.subplots(figsize=(4.8, 2.4))
ax.boxplot(np.log(counts_subset + 1))
ax.set_xlabel('Individuals')
ax.set_ylabel('log(Gene expression counts)')
reduce_xaxis_labels(ax, 5)
plt.show()

# Normalize by lib size
counts_lib_norm = counts / total_counts * 1000000
counts_subset_lib_norm = counts_lib_norm[:, samples_index]
fig, ax = plt.subplots(figsize=(4.8, 2.4))
ax.boxplot(np.log(counts_subset_lib_norm + 1))
ax.set_xlabel('Individuals')
ax.set_ylabel('log(Gene expression counts)')
reduce_xaxis_labels(ax, 5)
plt.show()


def class_boxplot(data, classes, colors=None, **kwargs):
    '''Make a boxplot with boxes colored according to the class they belong to.
    Args:
      data (list<arraylike<float>>): input data. One boxplot will be generated
        for each element in <data>
      classes (list<str> with len equal to <data>): the class each distribution
        in <data> belongs to.
      **kwargs: optional args to pass into <plt.boxplot>
    '''
    all_classes = sorted(set(classes))
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    class2color = dict(zip(all_classes, it.cycle(colors)))
    # map classes to data vectors; other classes get empty list at that position
    # to offset
    class2data = defaultdict(list)
    for distrib, cls in zip(data, classes):
        for c in all_classes:
            class2data[c].append([])
        class2data[cls][-1] = distrib
    # Do each boxplot with appropiate color
    fix, ax = plt.subplots()
    lines = []
    for cls in all_classes:
        # set color for all elements of boxplot
        for key in ['boxprops', 'whiskerprops', 'flierprops']:
            kwargs.setdefault(key, {}).update(color=class2color[cls])
        box = ax.boxplot(class2data[cls], **kwargs)
        lines.append(box['whiskers'][0])
    ax.legend(lines, all_classes)
    return ax


log_counts_3 = list(np.log(counts.T[:3] + 1))
log_ncounts_3 = list(np.log(counts_lib_norm.T[:3] + 1))
ax = class_boxplot(log_counts_3 + log_ncounts_3,
                   ['raw counts']*3 + ['normalized by lib size']*3,
                   labels=[1, 2, 3, 1, 2, 3])
ax.set_xlabel('sample number')
ax.set_ylabel('log(gene expression counts)')
plt.show()


# * forces following args to be keyword args
def binned_boxplot(x, y, *, xlabel='log(gene len)', ylabel='mean log counts'):
    '''Plot the distribution of <y> dependent on <x> with multiple boxplots.
    Note: All inputs expected to be log-scaled.
    Args:
      x (1D array<float>): independent variable values
      y (1D array<float>): dependent variable values
    '''
    x_hist, x_bins = np.histogram(x, bins='auto')
    x_bins_idxs = np.digitize(x, x_bins[:-1])
    binned_y = [y[x_bins_idxs == i] for i in range(x_bins_idxs.max())]
    fig, ax = plt.subplots(figsize=(4, 8.1))
    x_bin_centers = (x_bins[1:] + x_bins[:-1]) / 2
    x_ticklabels = np.round(np.exp(x_bin_centers)).astype(int)
    ax.boxplot(binned_y, labels=x_ticklabels)
    reduce_xaxis_labels(ax, 10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


log_counts = np.log(counts_lib_norm + 1)
mean_log_counts = np.mean(log_counts, axis=1)
log_gene_lengths = np.log(gene_lengths)
binned_boxplot(x=log_gene_lengths, y=mean_log_counts)
plt.show()

# longer genes have longer counts--an artifact of the lab method, not the
# biology, hence....


# Normalizing over Samples and Genes (RPKM: reads per kilobase transcripts per
# million)
C = counts
N = counts.sum(axis=0)
L = gene_lengths
C_tmp = 10**9 * C
print('C_tmp shape:', C_tmp.shape)
print('L shape:', L.shape)

L = L[:, np.newaxis] # append dim to L, with value 1
print('L.shape:', L.shape)

# Divide ea row by the gene len for that gene (L)
C_tmp = C_tmp / L
N = counts.sum(axis=0) # sum ea col = reads per sample
print('N.shape')
N = N[np.newaxis, :]
print('N.shape')

rpkm_counts = C_tmp / N


# all this is wrapped in the rpkm() function above


counts_rpkm = rpkm(counts, gene_lengths)
log_counts = np.log(counts + 1)
mean_log_counts = np.mean(log_counts, axis=1)
log_gene_lengths = np.log(gene_lengths)
binned_boxplot(x=log_gene_lengths, y=mean_log_counts)
plt.show()

log_counts = np.log(counts_rpkm + 1)
mean_log_counts = np.mean(log_counts, axis=1)
log_gene_lengths = np.log(gene_lengths)
binned_boxplot(x=log_gene_lengths, y=mean_log_counts)
plt.show()

gene_idxs = np.array([80, 186])
gene1, gene2 = gene_names[gene_idxs]
len1, len2 = gene_lengths[gene_idxs]
gene_labels = [f'{gene1}, {len1}bp', f'{gene2}, {len2}bp']
log_counts = list(np.log(counts[gene_idxs] + 1))
log_ncounts = list(np.log(counts_rpkm[gene_idxs] + 1))
ax = class_boxplot(log_counts, ['raw counts'] * 3, labels=gene_labels)
ax.set_xlabel('Genes')
ax.set_ylabel('log gene expression counts over all samples')
plt.show()

ax = class_boxplot(log_ncounts, ['RPKM normalized'] * 3, labels=gene_labels)
ax.set_xlabel('Genes')
ax.set_ylabel('log RPKM gene expression counts over all samples')
plt.show()
