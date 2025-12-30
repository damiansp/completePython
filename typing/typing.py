from collections.abc import Awaitable, Callable, Iterable, Mapping, Sequence
from typing import NewType, Protocol, TypeVar


def surface_area_of_cube(dim: float) -> str:
    area = 6 * dim**2
    return f'The surface area of the cube is {area}'


type Vector = list[float]


def scale(scalar: float, vec: Vector) -> Vector:
    return [scalar * n for n in vec]

new_vec = scale(2., [1., -4.2, 5.4])
print(new_vec)


type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]


def broadcast_msg(msg: str, servers: Sequence[Server]) -> None:
    pass


UserID = NewType('UserID', int)
some_id = UserID(524313)


def get_user_name(user_id: UserID) -> str:
    pass

user_a = get_user_name(UserID(42351))  # ok
user_b = get_user_name(42351)          # fails, int is not UserID

output = UserID(711) + UserID(177)     # output of type int, not UserID


# fails at runtime, does not pass type checking
class AdminUserID(UserID):
    pass


ProUserID = NewType('ProUserID', UserID)  # ok


def feeder(get_next_item: Callable[[], str]) -> None:
    pass


def async_query(
        on_success: Callable[[int], None],
        on_error: Callable[[int, Exception], None]
): -> None:
    pass


async def on_update(val: str) -> None:
    pass


callback: Callable[[str], Awaitable[None]] = on_update


def concat(x: str, y: str) -> str:
    return x + y


x: Callable[..., str]
x = str     # ok
x = concat  # ok


class Combiner(Protocol):
    def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]:
        pass


def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
    for item in data:
        pass


def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
    pass

# def bad_cb(*vals: byte, maxitem: int | None) -> list[bytes]: ...


batch_proc([], good_cb)   # ok
# batch_proc([], bad_cb)  # err: arg 2 incompaitble type bc of diff name/kind


class Employee:
    pass


# Sequence[Employee] indicates that all elems in the seq must be instances of
# "Employee". Mapping[str, str] indicates that all keys and vals must be strs
def notify_by_email(
        employees: Sequence[Employee], overrides: Mapping[str, str]
) -> None:
    pass


def first[T](l: Sequence[T]) -> T:
    return l[0]


U = TypeVar('U')


def econd(l: Sequence[U]) -> U:
    return l[1]
