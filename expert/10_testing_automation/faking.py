from collections import Counter
from typing import Dict


class AcmeSession:
    def __init__(self, tenant: str, token: str):
        pass


class AcmeHashMap:
    def __init__(self, acme_session: AcmeSession):
        pass

    def incr(self, key: str, amt):
        pass

    def atomic_incr(self, key: str, amt):
        pass

    def top_keys(self, count: int) -> Dict[str, int]:
        pass


class AcmeHashMapFake:
    def __init__(self):
        self._counter = Counter()

    def atomic_incr(self, key: str, amt):
        self._counter[key] += amt

    def top_keys(self, count: int) -> Dict[str, int]:
        return dict(self._counter.most_common(count))


# in some other module...
import pytest

from backends import
from acme_fakes import AcmeHashMapFake


@pytest.fixture
def acme_client():
    return AcmeHashMapFake()


@pytest.fixture
def acme_backend(acme_client):
    return AcmeBackend(acme_client)
