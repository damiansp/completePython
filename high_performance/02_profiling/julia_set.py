'Julia Set generator w/o image drawing'
import time


# area of complex space to investigate
x1, x2 = -1.8, 1.8
y1, y2 = -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def calc_pure_python(width, max_iters):
    '''Create a list of complex coords (zs) and complex params (cs), build
    Julia set
    '''
    x_step = (x2 - x1) / width
    y_step = (y2 - y1) / width
    x, y = [], []
    y_coord = y2
    while y_coord > y1:
        y.append(y_coord)
        y_coord += y_step
    x_coord = x1
    while x_coord < x2:
        x.append(x_coord)
        x_coord += x_step
    # build a list of coords and the init condition for each cell. Note that
    # init conditio is a const and could be removed; used to simulate a real-
    # world scenario w several inputs to our func
    zs, cs = [], []
    for y_coord in y:
        for x_coor in x:
            zs.append(complex(x_coord, y_coord))
            cs.append(complex(c_real, c_imag))
    print('len(x):', len(x))
    print('Total elems:', len(zs))
    start = time.time()
    out = calculate_z_serial_purepython(max_iters, zs, cs)
    end = time.time()
    secs = end - start
    print(f'{calculate_z_serial_purepython.__name__} took {secs} s')
    assert sum(out) == 33219980
