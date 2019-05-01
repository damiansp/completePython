# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# summary is required, owner & done are optional, id set by DB
import pytest

import tasks
from tasks import Task


@pytest.fixture()
def tasks_just_a_few():
    '''All summaries and owners are unique'''
    return (Task('write some code', 'Cody', True),
            Task('review cody\'s code', 'Reggie', False),
            Task('fix reggie\'s flaws', 'Fiona', False))


@pytest.fixture()
def tasks_mult_per_owner():
    '''Several owners with several tasks each'''
    return(Task('make cookies', 'Raphael'),
           Task('emote', 'Raphael'),
           Task('move to berlin', 'Raphael'),
           Task('multilpy', 'Michelle'),
           Task('magnify', 'Michelle'),
           Task('minimize', 'Michelle'),
           Task('dance', 'Daniel'),
           Task('destroy', 'Daniel'),
           Task('devestate', 'Daniel'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    '''Connected DB with 3 fully unique tasks'''
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_mult_per_owner(tasks_db, tasks_mult_per_owner):
    '''Connected DB with 9 tasks with 3 owners, each with 3 tasks'''
    for t in tasks_mult_per_owner:
        tasks.add(t)
