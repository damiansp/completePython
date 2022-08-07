from itertools import combinations
import sys

from static import BODIES


TIMESTEP = 0.01


def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    pairs = combinations(system, 2)
    offset_momentum(bodies[ref], system)
    report_energy(system, pairs)
    advance(TIMESTEP, n, system, pairs)
    report_energy(system, pairs)
    
    
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


def report_energy(bodies, pairs):
    e = 0.
    for ((p1, v1, m1), (p2, v2, m2)) in pairs:
        dx, dy, dz = get_deltas(p1, p2)
        e -= (m1 * m2) / ((dx*dx + dy*dy + dz*dz) ** 0.5)
    for (r, [vx, vy, vz], m) in bodies:
        e += m * (vx*vx + vy*vy + vz*vz) / 2.
    print(f'{e:.9f}')


def advance(dt, n, bodies, pairs):
    for i in range(n):
        for ((p1, v1, m1), (p2, v2, m2)) in pairs:
            dx, dy, dz = get_deltas(p1, p2)
            mag = dt * ((dx*dx + dy*dy + dz*dz) ** (-1.5))
            b1m = m1 * mag
            b2m = m2 * mag
            v1[0] -= dx * b2m
            v1[1] -= dy * b2m
            v1[2] -= dz * b2m
            v2[0] -= dx * b1m
            v2[1] -= dy * b1m
            v2[2] -= dz * b1m
        for (r, [vx, vy, vz], m) in bodies:
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz

            
def get_deltas(p1, p2):
    return [a - b for a, b in zip(p1, p2)]


if __name__ == '__main__':
    main(int(sys.argv[1]))
