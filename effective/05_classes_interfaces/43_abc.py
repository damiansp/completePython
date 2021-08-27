from collections.abc import Sequence


class FreqList(list):
    def __init__(self, members):
        super().__init__(members)

    def freq(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


foo = FreqList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('Len:', len(foo))
print('Freqs:', foo.freq())
print('Popping...')
foo.pop()
print('Len:', len(foo))
print('Freqs:', foo.freq())


class BinaryNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


bar = [1, 2, 3]
bar[0] # => bar.__getitem__(0)


class IndexableNode(BinaryNode):
    def _traverse(self):
        '''Traversal is depth-first'''
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()

    def __getitem__(self, index):
        '''Makes tree list-like'''
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.val
        raise IndexError(f'Index {index} is out of range')


#      10
#     /  \
#    /    \
#   5      15
#  / \    /  
# 2   6  11
#      \
#       7

tree = IndexableNode(
    10,
    left=IndexableNode(
        5,
        left=IndexableNode(2),
        right=IndexableNode(
            6,
            right=IndexableNode(7))),
    right=IndexableNode(
        15,
        left=IndexableNode(11)))
print('Tree list:', list(tree))
print('LRR:', tree.left.right.right.val)
print('Index 0:', tree[0])
print('Index 1:', tree[1])
#print('Index -1:', tree[-1]) # not implemented
print('11 in tree:', 11 in tree)
print('17 in tree:', 17 in tree)

# but...
# len(tree) # TypeError, must add __len__


class SequenceNode(IndexableNode):
    def __len__(self):
        for count, _ in enumerate(self._traverse(), 1):
            pass
        return count

    
tree = SequenceNode(
    10,
    left=SequenceNode(
        5,
        left=SequenceNode(2),
        right=SequenceNode(
            6,
            right=SequenceNode(7))),
    right=SequenceNode(
        15,
        left=SequenceNode(11)))

print('Tree length:', len(tree))


#class BadType(Sequence):
#    pass

#foo = BadType() # TypeError Can't instantiate abstract class BadType with
#                # abstract methods __getitem__, __len__


class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(
    10,
    left=BetterNode(
        5,
        left=BetterNode(2),
        right=BetterNode(
            6,
            right=BetterNode(7))),
    right=BetterNode(
        15,
        left=BetterNode(11)))

print('Index of 7:', tree.index(7))
print('Count of 10:', tree.count(10))


