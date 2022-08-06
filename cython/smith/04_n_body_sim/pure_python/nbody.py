from itertools import combinations
import sys

from static import BODIES


def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    pairs = combinations(system, 2)
    offset_momentum(bodes[ref], system)
    report_energy(bodies, pairs)

    
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
    


if __name__ == '__main__':
    main(int(sys.argv[1]))
