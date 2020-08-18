from collections.abc import MutableMapping
from typing import Dict, MutableMapping as MM


votes = {'otter': 1281, 'polar bear': 587, 'fox': 863}


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks):
    return next(iter(ranks))


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)


# Suppose criterion changes st we now want alphabetical ordering...
class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner) # wrong: get_winner() assumes dict's iteration is insert order


def get_winner_robust(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name

winner = get_winner_robust(sorted_ranks)
print(winner)
    

# Better runtime
def get_winner_faster(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('must provide a dict instance')
    return next(iter(ranks))

#get_winner_faster(sorted_ranks) # throws error


def populate_ranks_annotated(
        votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(vote.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner_annotated(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))

# ...
