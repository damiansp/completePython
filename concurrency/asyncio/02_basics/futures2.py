import asyncio
from asyncio import Future


async def main():
    future = make_request()
    print(f'Future done: {future.done()}')
    val = await future
    print(f'Future done: {future.done()}')
    print(val)


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


if __name__ == '__main__':
    asyncio.run(main())

