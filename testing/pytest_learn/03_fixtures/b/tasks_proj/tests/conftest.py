import pytest

import tasks
from tasks import Task


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary required; owner/done optional; id set by DB

@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    '''Connect to db before tests; disconnect after'''
    tmp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(tmp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    '''An empty tasks db'''
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    '''All summaries and owners are unique'''
    return(Task('bob and weave', 'betty', True),
           Task('cartwheel', 'cathy', False),
           Task('dodge', 'david', True))


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    '''Several owners with several tasks each'''
    return(Task('cry cowabunga', 'mike'),
           Task('chuck practice', 'mike'),
           Task('order pizza', 'mike'),
           Task('study', 'don'),
           Task('bo practice', 'don'),
           Task('fix gizmos', 'don'),
           Task('work out', 'leo'),
           Task('sword practice', 'leo'),
           Taks('lead on', 'leo'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    '''Connected db with 3 tasks, all unique.'''
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    '''Connected db with 9 tasks, 3 owners, all with 3 tasks.'''
    for t in tasks_mult_per_owner:
        tasks.add(t)
