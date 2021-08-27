import datetime
import random
import time
from collections import namedtuple

import pytest


#@pytest.fixture(autouse=True)
#def check_duration(request, cache):
    # nodeid's can have colons
    # keys become filenames in .cache
    # replace colons with something filename-safe
#    key = 'duration/' + request.node.nodeid.replace(':', '_')
#    start_time = datetime.datetime.now()
#    yield
#    stop_time = datetime.datetime.now()
#    this_duration = (stop_time - start_time).total_seconds()
#    last_duration = cache.get(key, None)
#    cache.set(key, this_duration)
#    if last_duration is not None:
#        errorstring = 'test duration over 2x last duration'
#        assert this_duration <= last_duration * 2, errorstring


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())

duration = namedtuple('Duration', ['current', 'last'])


@pytest.fixture(scope='session')
def duration_cache(request):
    key = 'duration/testdurations'
    d = duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    node_id = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[node_id] = duration
    if d.last.get(node_id, None) is not None:
        errorstring = 'test duration > 2x last duration'
        assert duration <= (d.last[node_id] * 2), errorstring
