import asyncio


async def add_one(n: int) -> int:
    return n + 1


async def main() -> None:
    two = await add_one(1)
    three = await add_one(2)
    print(two)
    print(three)


if __name__ == '__main__':
    asyncio.run(main())
