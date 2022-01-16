# module-level __getattr__() and __dir__()
from typing import Any
from warnings import warn


def ci_lookup(d: dict[str, Any], key: str) -> Any:
    # ...
    pass

def __getattr__(name: str):
    if name == 'get_ci':
        warn(f'{name} is deprecated', DeprecationWarning)
        return ci_lookup
    raise AttributeError(f'module {__name__} has no attribute {name}')

