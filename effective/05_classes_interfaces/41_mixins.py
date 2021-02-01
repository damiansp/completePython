from pprint import pprint


class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        out = {}
        for k, v in instance_dict.items():
            out[k] = self._traverse(k, v)
        return out

    def _traverse(self, key, val):
        if isinstance(val, ToDictMixin):
            return val.to_dict()
        if isinstance(val, dict):
            return self._traverse_dict(val)
        if isinstance(val, list):
            return [self._traverse(key, i) for i in val]
        if hasattr(val, '__dict__'):
            return self._traverse_dict(val.__dict__)
        return val


class BinaryTree(ToDictMixin):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = BinaryTree(10,
                  left=BinaryTree(7, right=BinaryTree(9)),
                  right=BinaryTree(13, left=BinaryTree(11)))
pprint(tree.to_dict())


class BinaryTreeWithParent(BinaryTree):
    def __init__(self, val, left=None, right=None, parent=None):
        super().__init__(val, left=left, right=right)
        self.parent = parent

    # overwrite _traverse to prevent inf loop
    def _traverse(self, key, val):
        if isinstance(val, BinaryTreeWithParent) and key == 'parent':
            return val.val # prevent cycling
        return super()._traverse(key, val)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7, parent=root)
root.left.right = BinaryTreeWithParent(9, parent=root.left)
pprint(root.to_dict())
