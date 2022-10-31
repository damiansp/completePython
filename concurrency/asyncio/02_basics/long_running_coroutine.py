import asyncio


async def main() -> None:
    msg = await get_msg()
    print(msg)


async def get_msg() -> str:
    await asyncio.sleep(1)
    return 'Hello, World!'


if __name__ == '__main__':
    asyncio.run(main())
