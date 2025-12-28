from collections.abc import Sequence
from typing import NewType


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

