import asyncio
import sys

sys.path.append('..')
from util import async_timed


async def main() -> None:
    task_one = asyncio.create_task(do_cpu_work())
    await task_one


@async_timed()
async def do_cpu_work() -> int:
    counter = 0
    for _ in range(100_000_000):
        counter += 1
    return counter


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
