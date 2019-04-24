"""Main API for tasks project."""

from collections import namedtuple
from six import string_types


# Task element types : [summary: str, owner: str, done: bool, id: int]
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
