def main(n, bodies=BODIES, ref='sun'):
    system = list(bodies.values())
    pairs = combinations(system)
    offset_momentum(bodies[ref], system)
    report_energy(system, pairs)
    advance(0.01, n, system, pairs)
    report_energy(system, pairs)
