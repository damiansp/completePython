sun = (
    [0., 0., 0.],  # pos
    [0., 0., 0.],  # vel
    SOLAR_MASS)
jupiter = (
    [4.84143144246472090e+00,
     -1.16032004402742839e+00,
     -1.03622044471123109e-01],
    [1.66007664274403694e-03 * DAYS_PER_YEAR,
     7.69901118419740425e-03 * DAYS_PER_YEAR,
     -6.90460016972063023e-05 * DAYS_PER_YEAR],
    9.54791938424326609e-04 * SOLAR_MASS)
       

def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    pairs = combinations(system)
    offset_momentum(bodies[ref], system)
    report_energy(system, pairs)
    advance(0.01, n, system, pairs)
    report_energy(system, pairs)


def advance(dt, n, bodies, pairs):
    for i in range(n):
        for (([x1, y1, z1], v1, m1), ([x2, y2, z2], v2, m2)) in pairs:
            # update velocities...
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
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
            # update positions
            r[0] += dt * vx
            r[1] += dt * vy
            r[2] += dt * vz


# cython version
def advance(double dt, int n, bodies):
    cdef:
        int i, ii, jj
        double dx, dy, dz, mag, b1m, b2m
        body_t *body1
        body_t *body2
        body_t cbodies[N_BODIES]
    make_cbodies(bodies, cbodies, N_BODIES)
    for i in range(n):
        for ii in range(N_BODIES - 1):
            body1 = &cbodies[ii]
            for jj in range(ii + 1, N_BODIES):
                body2 = &cbodies[jj]
                dx = body1.x[0] - body2.x[0]
                dy = body1.x[1] - body2.x[1]
                dz = body1.x[2] - body2.x[2]
                mag = dt * ((dx*dx + dy*dy + dz*dz)**(-1.5))
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



cdef struct body_t:
    double x[3]
    double v[3]
    double m


cdef void make_cbodies(list bodies, body_t *cbodies, int n_cbodies):
    cdef body_t *cbody
    for i, body in enumerate(bodies):
        if i >= n_cbodies:
            break
        (x, v, m) = body
        cbody = &cbodies[i]
        cbody.x[0], cbody.x[1], cbody.x[2] = x
        cbody.v[0], cbody.v[1], cbody.v[2] = v
        cbodies[i].m = m


cdef list make_pybodies(body_t *cbodies, int n_bodies):
    pybodies = []
    for i in range(n_cbodies):
        x = [cbodies[i].x[0], cbodies[i].x[1], cbodies[i].x[2]]
        v = [cbodies[i].v[0], cbodies[i].v[1], cbodies[i].v[2]]
        pybodies.append((x, v, cbodies[i].m))
    return pybodies
