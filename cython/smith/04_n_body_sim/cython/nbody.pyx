from itertools import combinations
import sys

from libc.math cimport pow, sqrt

from static import BODIES


DEF N_BODIES = 5


cdef struct body_t:
    double x[3]
    double v[3]
    double m


def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    offset_momentum(bodies[ref], system)
    report_energy(system)
    system = advance(0.01, n, system)
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


def advance(double dt, int n, bodies):
    cdef:
        int i, ii, jj
        double dx, dy, dz, mag, b1m, b2m, ds
        body_t *body1
        body_t *body2
        body_t cbodies[N_BODIES]
    make_cbodies(bodies, cbodies, N_BODIES)
    for i in range(n):
        for ii in range(N_BODIES -1):
            body1 = &cbodies[ii]
            for jj in range(ii + 1, N_BODIES):
                body2 = &cbodies[jj]
                dx = body1.x[0] - body2.x[0]
                dy = body1.x[1] - body2.x[1]
                dz = body1.x[2] - body2.x[2]
                ds = dx*dx + dy*dy + dz*dz
                mag = dt / (ds * sqrt(ds))
                b1m = body1.m * mag
                b2m = body2.m * mag
                body1.v[0] -= dx * b2m
                body1.v[1] -= dy * b2m
                body1.v[2] -= dz * b2m
                body2.v[0] -= dx * b1m
                body2.v[1] -= dy * b1m
                body2.v[2] -= dz * b1m
        for ii in range(N_BODIES):
            body2 = &cbodies[ii]
            body2.x[0] += dt * body2.v[0]
            body2.x[1] += dt * body2.v[1]
            body2.x[2] += dt * body2.v[2]
    return make_pybodies(cbodies, N_BODIES)


cdef void make_cbodies(list bodies, body_t *cbodies, int n_cbodies):
    cdef body_t *cbody
    for i, body in enumerate(bodies):
        if i >= n_cbodies:
            break
        x, v, m = body
        cbody = &cbodies[i]
        cbody.x[0], cbody.x[1], cbody.x[2] = x
        cbody.v[0], cbody.v[1], cbody.v[2] = v
        cbodies[i].m = m    


cdef list make_pybodies(body_t *cbodies, int n_cbodies):
    pybodies = []
    for i in range(n_cbodies):
        x = [cbodies[i].x[0], cbodies[i].x[1], cbodies[i].x[2]]
        v = [cbodies[i].v[0], cbodies[i].v[1], cbodies[i].v[2]]
        pybodies.append((x, v, cbodies[i].m))
    return pybodies
