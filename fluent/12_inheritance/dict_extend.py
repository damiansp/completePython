import collections


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict(one=1)
print(dd) # {'one': 1}

dd['two'] = 2
dd.update(three=3)

print(dd) # {'one': 1, 'two': [2, 2], 'three': 3}



class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a='foo')
print(ad['a']) # 42

d = {}
d.update(ad)
print(d['a']) # foo
print(d)      # {'a': 'foo'}



class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict2(one=1)
print(dd) # {'one': [1, 1]}

dd['two'] = 2
dd.update(three=3)

print(dd) # {'one': [1, 1], 'two': [2, 2], 'three': [3, 3])



class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict2(a='foo')
print(ad['a']) # 42

d = {}
d.update(ad)
print(d['a']) # 42
print(d)      # {'a': 42}


                
