from itertools import combinations
import sys

from libc.math cimport pow, sqrt

from static import BODIES


DEF N_BODIES = 5


def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    offset_momentum(bodies[ref], system)
    report_energy(system)
    system = advance(0.01, n, system)


def offset_momentum(ref, bodies):
    px = py = pz = 0.
    for (r, [vx, vy, vz], m) in bodies:
        px -= vx * m
        py -= vy * m
        pz -= vz * m
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def report_energy(bodies):
    e = 0.
    pairs = combinations(bodies, 2)
    for (((x1, y1, z1), v1, m1), ((x2, y2, z2), v2, m2)) in pairs:
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        e -= (m1 * m2) / ((dx*dx + dy*dy + dz*dz) ** 0.5)
    for (r, [vx, vy, vz], m) in bodies:
        e += m * (vx*vx + vy*vy + vz*vz) / 2.
    print(f'{e:.9f}')


def advance():
    pass
