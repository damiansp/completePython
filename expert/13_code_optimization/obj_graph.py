from collections import Counter

import objgraph


def graph_references(*objs):
    objgraph.show_refs(
        objs,
        filename='show_refs.png',
        refcounts=True,
        too_many=5, # filter for brevity here
        filter=lambda x: not isinstance(x, dict))
    objgraph.show_backrefs(objs, filename='show_backrefs.pbg', refcounts=True)


if __name__ == '__main__':
    quote = (
        'People who think they know everything are a great annoyance to those '
        'of us who do.')
    words = quote.lower().split()
    counts = Counter(words)
    graph_references(words, quote, counts)
