from pprint import pprint


class Person:
    def __init__(self, name):
        self.name = name


class DictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, attributes: dict) -> dict:
        res = {}
        for k, v in attributes.items():
            res[k] = self._traverse(k, v)
        return res

    def _traverse(self, key, val):
        if isinstance(val, DictMixin):
            return val.to_dict()
        if isinstance(val, dict):
            return self._traverse_dict(val)
        if isinstance(val, list):
            return [self._traverse(key, v) for v in val]
        if hasattr(val, '__dict__'):
            return self._traverse_dict(val.__dict__)
        return val


class Employee(DictMixin, Person):
    def __init__(self, name, skills, dependents):
        super().__init__(name)
        self.skills = skills
        self.dependents = dependents


if __name__ == '__main__':
    e = Employee(
        'John',
        skills=['Python Programming', 'Sausage Buttering'],
        dependents={'wife': 'Jane', 'children': ['Alice', 'Bob']})
    pprint(e.to_dict())
    
