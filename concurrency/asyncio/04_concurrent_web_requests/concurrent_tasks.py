import asyncio
import sys

sys.path.append('..')
from util import async_timed, delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]

    # Nope:
    #[await asyncio.create_task(delay(seconds)) for seconds in delay_times]

    # Yep:
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


if __name__ == '__main__':
    asyncio.run(main())


