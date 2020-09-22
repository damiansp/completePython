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
