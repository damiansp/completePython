import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    '''Connect to db before test; disconnect after'''
    # Setup: start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield # testing happens here
    # Teardown: stop db
    tasks.stop_tasks_db()
    
