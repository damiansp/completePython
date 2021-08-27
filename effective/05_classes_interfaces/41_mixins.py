import json
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


class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent

my_tree = NamedSubTree('foobar', root.left.right)
print(my_tree.to_dict())


class JsonMixin:
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())


class DatacenterRack(ToDictMixin, JsonMixin):
    def __init__(self, switch=None, machines=None):
        self.switch = Switch(**switch)
        self.machines = [Machine(**kwargs) for kwargs in machines]


class Switch(ToDictMixin, JsonMixin):
    def __init__(self, ports=None, speed=None):
        self.ports = ports
        self.speed = speed


class Machine(ToDictMixin, JsonMixin):
    def __init__(self, cores=None, ram=None, disk=None):
        self.cores = cores
        self.ram = ram
        self.disk = disk

serialized = '''{
    "switch": {"ports": 5, "speed": 1e9},
    "machines": [{"cores": 8, "ram": 32e9, "disk":   5e12},
                 {"cores": 4, "ram": 16e9, "disk":   1e12},
                 {"cores": 2, "ram":  4e9, "disk": 500e9 }]
}'''
deserialized = DatacenterRack.from_json(serialized)
roundtrip = deserialized.to_json()
assert json.loads(serialized) == json.loads(roundtrip), 'somethin aint right'
