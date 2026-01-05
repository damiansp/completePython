# From Ref: https://docs.python.org/3.13/library/typing.html
from collections.abc import (
    Awaitable, Callable, Coroutine, Iterable, Mapping, Sequence, Sized)
from logging import Logger
from typing import Generic, NewType, Protocol, Sequence as SeqType, TypeVar


def surface_area_of_cube(dim: float) -> str:
    area = 6 * dim**2
    return f'The surface area of the cube is {area}'



# Type Aliases ----------
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


# New Type ----------
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


# Annotating Callables ----------
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



# Generics ----------
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



# Annotating Tuples ---------
x: list[int] = []
# y: list[int, str] = [1, 'foo']  # type checker error
z: Mapping[str, str | int] = {}

x: tuple[int] = (5,)
y: tuple[int, str] = (5, 'foo')  # ok
#z: tuple[int] = (1, 2, 3)       # err, annotated for one val only

x: tuple[int, ...] = (1, 2)  # ok
x = (1, 2, 3)                # reassignment ok
x = ()                       # ok
x = ('foo', 'bar')           # err
y: tuple[()] = ()            # can only be an empty tuple
z: tuple('foo', 'bar')
z = (1, 2, 3)                # ok
z = ()                       # ok


class User:
    pass


class ProUser(User):
    pass


class TeamUser(User):
    pass


def make_new_user(user_class: type[User]) -> User:
    # ...
    return user_class()


make_new_user(User)      # ok
make_new_user(ProUser)   # ok
make_new_user(TeamUser)  # ok
# make_new_user(User())  # err: expected <type[User]> but got <User>
# make_new_user(int)     # err: <type[int]> not a subtype of <type[User]>


def new_non_team_user(user_class: type[BasicUser | ProUser]):
    pass


new_non_team_user(BasicUser)  # ok
new_non_team_user(ProUser)    # ok
new_non_team_user(TeamUser)   # err
new_non_team_user(User)       # err


# Annotating generators and coroutines ----------
# Generator[YieldType, SendType, ReturnType]
def echo_round() -> Generator[int, float, str]:  
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'


def inifinite_stream(start: int) -> Generator[int]:  #  = [int, None, None]
    while True:
        yield start
        start += 1


# if only ever yields vals, Iterable/Iterator ok too
def inf_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1


# AsyncGenerator[YieldType, SendType=None]
async def infinite_strem(start: int) -> AsyncGenerator[int]:
    while True:
        yield start
        start += 1


# Couroutine[YieldType, SendType, ReturnType]
c: Couroutine[list[str], str, int]  # some couroutine defined elsewhere
x = c.send('hi')                   # inferred type of <x> is list[str]


async def bar() -> none:
    y = await c  # inferred type of <y> is int


# User-defined generic types ----------
class LoggedVar[T]:
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log(f'Set {repr(self.value)}')
        self.value = new

    def get(self): -> T:
        self.log(f'Get {repr(self.value)}')
        return self.value

    def log(self, msg: str) -> None:
        self.logger.infor(f'{self.name}: {msg}')


T = TypeVar('T')


# <=3.11 compatibility
class LoggedVar(Generic[T]):
    pass


def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)


class WeirdTrio[T, B: SeqType[bytes], S: (int, str)]:
    pass


OldT = TypeVar('OldT', contravariant=True)
OldB = TypeVar('OldB', bound=SeqType[bytes], covariant=True)
OldS = TypeVar('OldS', int, str)


class OldWeirdTrio(Generic[OldT, OldB, OldS]):
    pass


# class Pair[M, M]:  # Syntax err

T = TypeVar('T')

# class Pair(Generic[T, T]):  # invalid; eac type var arg must be distinct


class LinkedList[T](Sized):
    pass


class MyDict[T](Mapping[str, T]):
    pass


class MyIterable(Iterable):  # same as Iterable[Any]
    pass


type Response[S] = Iterable[S] | int

# Return type here same as Iterable[str] | int
def response(query: str) -> Response[str]:
    pass


type Vec[T] = Iterable[tuple[T, T]]


# return type same as Iterable[tuple[T, T]]
def inprod[T: (int, float, complex)](v: Vec[T]) -> T:
    return sum(x * y for x, y in v)


