import asyncio
import sys

sys.path.append('..')
from util.delay_functions import delay


async def incr(n: int) -> int:
    return n + 1


async def get_msg() -> str:
    await delay(1)
    return 'Hello, World!'


async def main() -> None:
    msg = await get_msg()
    deux = await incr(1)
    print(f'deux is {deux}')
    print(msg)


if __name__ == '__main__':
    asyncio.run(main())
