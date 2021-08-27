import pytest

import tasks
from tasks import Task


@pytest.fixture(scope='session', params=['tiny', 'mongo'])
def tasks_db_session(tmpdir_factory, requests):
    '''Connect to db before tests, disconnect after'''
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    '''An empty tasks db'''
    tasks.delete_all()
