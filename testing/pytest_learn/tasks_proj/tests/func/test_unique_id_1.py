import pytest

import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    '''Connect to db before testing, disconnect after.'''
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield # testing happens here
    # Teardown: stop db
    tasks.stop_tasks_db()


@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported pre 0.2.0')
def test_unique_id():
    '''Calling unique_id() twice should return different numbers'''
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                   reason='not supported until 0.2.0')
def test_unique_id_1():
    '''Calling unique_id() twice should return different numbers'''
    id1 = tasks.unique_id()
    id2 = tasks.unique_id()
    assert id1 != id2


def test_unique_id2():
    '''unique_id() should return an unused id.'''
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    uid = tasks.unique_id()
    assert uid not in ids


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    '''xfail demo'''
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_is_not_a_duck():
    '''xpass demo'''
    uid = tasks.unique_id()
    assert uid != 'a duck'
