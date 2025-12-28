def main():
    tree = BinaryTree(
        4,
        BinaryTree(2, BinaryTree(1), BinaryTree(3)),
        BinaryTree(6, BinaryTree(5), BinaryTree(7)))
    for val in InOrderIterator(tree):
        print(val)
        

class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class InOrderIterator:
    def __init__(self, root):
        self.stack = []
        self.current = root

    def __iter__(self):
        return self

    def __next__(self):
        while self.current or self.stack:
            if self.current:
                self._get_from_current()
            else:
                return self._get_from_stack()
        raise StopIteration  # back one indent?

    def _get_from_current(self):
        self.stack.append(self.current)
        self.current = self.current.left

    def _get_from_stack(self):
        node = self.stack.pop()
        res = node.val
        self.current = node.right
        return res


if __name__ == '__main__':
    main()
