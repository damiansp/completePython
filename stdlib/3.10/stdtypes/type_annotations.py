from typing import TypeVar

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
