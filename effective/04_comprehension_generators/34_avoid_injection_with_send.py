import math


def wave(amp, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        rad = step * step_size
        frac = math.sin(rad)
        out = amp * frac
        yield out


def transmit(output):
    if output is None:
        print('No  output')
    else:
        print(f'Output: {output:>5.1f}')


def run(it):
    for out in it:
        transmit(out)

run(wave(3.0, 8))



def my_generator():
    received = yield 1
    print(f'Received: {received}')

it = iter(my_generator())
output = next(it) # 1st output generator output
print(f'output: {output}')
try:
    next(it)      # run generator until it exists
except StopIteration:
    pass


it = iter(my_generator())
out = it.send(None) # get 1st gen output
print(f'out: {out}')
try:
    it.send('hello!') # Send val into gen
except StopIteration:
    pass


def wave_mod(steps):
    step_size = 2 * math.pi / steps
    amp = yield # receive init amp
    for step in range(steps):
        rad = step * step_size
        frac = math.sin(rad)
        out = amp * frac
        amp = yield out


def run_mod(it):
    amps = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amp in amps:
        out = it.send(amp)
        transmit(out)

run_mod(wave_mod(12))


def complex_wave():
    yield from wave(7., 3)
    yield from wave(2., 4)
    yield from wave(10., 5)

run(complex_wave())


def complex_wave_mod():
    yield from wave_mod(3)
    yield from wave_mod(4)
    yield from wave_mod(5)

#run(complex_wave_mod()) # Err


def wave_cascading(amp_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        rad = step * step_size
        frac = math.sin(rad)
        amp = next(amp_it)
        out = amp * frac
        yield out


def complex_wave_cascading(amp_it):
    yield from wave_cascading(amp_it, 3)
    yield from wave_cascading(amp_it, 4)
    yield from wave_cascading(amp_it, 5)


def run_cascading():
    amps = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amps))
    for amp in amps:
        output = next(it)
        transmit(output)

run_cascading()
    
