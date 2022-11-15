import asyncio
import functools
import time
from typing import Any, Callable


async def delay(s: int) -> int:
    print(f'Sleeping for {s}s...')
    await asyncio.sleep(s)
    print(f'{s}s sleep complete.')
    return s


def async_timed():
    def wrapper(f: Callable) -> Callable:

        @functools.wraps(f)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Starting {f} with args {args} {kwargs}')
            start = time.time()
            try:
                return await f(*args, **kwargs)
            finally:
                elapsed = time.time() - start
                print(f'Finished {f} in {elapsed:.4f}s')
        return wrapped

    return wrapper

