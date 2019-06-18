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

