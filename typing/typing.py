from collections.abc import Sequence


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

