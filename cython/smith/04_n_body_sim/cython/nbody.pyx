import sys

from libc.math cimport pow, sqrt

from static import BODIES


DEF N_BODIES = 5


def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    offset_momentum(bodies[ref], system)
    report_energy(system)


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
    pass
