'''Test the Task data type.'''
from collections import namedtuple

import pytest


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    '''Using no parameters should invoke defaults.'''
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

@pytest.mark.my_mark # allow tests to be run by mark name
def test_member_access():
    '''Check .field functionality of namedtuple.'''
    t = Task('buy milk', 'Damian')
    assert t.summary == 'buy milk'
    assert t.owner == 'Damian'
    assert (t.done, t.id) == (False, None)


def test_asdict():
    '''_asdict() should return a dictionary.'''
    t_task = Task('exercise', 'jimbo', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'exercise',
                'owner': 'jimbo',
                'done': True,
                'id': 21}
    assert t_dict == expected


def test_replace():
    '''replace() should change passed in fields.'''
    t_before = Task('finish book', 'Damian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'Damian', True, 10)
    assert t_after == t_expected
