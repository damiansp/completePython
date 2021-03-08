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

