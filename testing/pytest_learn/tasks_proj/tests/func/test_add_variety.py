import pytest

import tasks
from tasks import Task


def test_add_1():
    '''tasks.get() using id returned from add() works.'''
    task = Task('breathe', 'brian', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    # everything but id should be the same
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task',
                         [Task('sleep', done=True),
                          Task('wake', 'wendy'),
                          Task('breathe', 'bradley'),
                          Task('exercise', 'erica', False)])
def test_add_2(task):
    '''Demonstrate parameterize with one parameter.'''
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done',
                         [('sleep', None, False),
                          ('wake', 'wendell', False),
                          ('breathe', 'brita', True),
                          ('eat eggs', 'englebert', False)])
def test_add_3(summary, owner, done):
    '''Demonstrate parameterize with multiple parameters.'''
    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)
    
tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'willie'),
                Task('xylophone', 'xerxes'),
                Task('yelp', 'yolanda', True),
                Task('zip', 'zach', False))


@pytest.mark.parametrize('task', tasks_to_try)
def test_add_4(task):
    '''Slightly different take'''
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

task_ids = [f'Task({t.summary}, {t.owner}, {t.done})' for t in tasks_to_try]


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
def test_add_5(task):
    '''Demonstrate ids.'''
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids)
class TestAdd():
    '''Demonstrate parametrize and test classes'''
    def test_equivalent(self, task):
        ''''Similar test, but in a class'''
        task_id = tasks.add(task)
        t_from_db = tasks.get(task_id)
        assert equivalent(t_from_db, task)


def test_valid_id(self, task):
    '''We can use the same data or multiple tests.'''
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert t_from_db.id == task_id


@pytest.mark.parametrize(
    'task',
    [pytest.param(Task('create'), id='just summary'),
     pytest.param(Task('inspire', 'ivan'), id='summary/owner'),
     pytest.param(Task('encourage', 'eileen', True), id='summary/owner/done')])
def test_add_6(task):
    '''Demonstrate pytest.param and id.'''
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert(equivalent(t_from_db, task))

    
def equivalent(t1, t2):
    '''Check two tasks for equivalence.'''
    # Compare everything but id field
    return ((t1.summary == t2.summary)
            and (t1.owner == t2.owner)
            and (t1.done == t2.done))


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    '''Connect to db before testing, disconnect after.'''
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()



    
