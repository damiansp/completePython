from typing import Optional, TypeVar, Union

def average(values: list[float]) -> float:
    return sum(values) / len(values)


def send_post_request(url: str, body: dict[str, int]) -> None:
    pass


t = list[str]
print(type(t))
l = t()
print(type(l))
print(l)


Y = TypeVar('Y')
print(dict[str, Y],[int])  # dict[str, int]


def square(n: int | float) -> int | float:
    return n ** 2


print(int | str == Union[int, str])  # True
print(str | None == Optional[str])   # True
