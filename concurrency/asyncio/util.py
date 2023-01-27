import asyncio
import functools
import time
from typing import Any, Callable

import aiohttp
from aiohttp import ClientSession


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


#async def fetch_status(session: ClientSession, url: str) -> int:
#    ten_ms = aiohttp.ClientTimeout(total=0.01)
#    async with session.get(url, timeout=ten_ms) as res:
#        return res.status


async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as res:
        return res.status
