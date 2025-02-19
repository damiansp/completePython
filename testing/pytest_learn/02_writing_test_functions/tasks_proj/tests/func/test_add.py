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

def test_add_returns_valid_id():
    '''tasks.add(<valid task>) should return an int.'''
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do dat')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    '''Make sure the task_id field is set by tasks.add()'''
    # GIVEN an initialized tasks db
    #   AND a new task is added
    new_task = Task('thrash about', owner='me', done=True)
    task_id = tasks.add(new_task)
    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)
    # THEN task_id matches id field
    assert task_from_db.id == task_id
