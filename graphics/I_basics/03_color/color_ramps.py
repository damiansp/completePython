import random
import sys
from tkinter import *

sys.path.append('../../')
from util import Point, rgb2hex


def main():
    root = Tk()
    root.title('')

    W, H = 1580, 200
    PAD = 20
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    start_point = Point(PAD, PAD)
    ramp_height = H - 2*PAD
    n_steps = 255

    r1, r2, r3, r4, g1, g2, g3, g4, b1, b2, b3, b4 = (
        [random.uniform(0., 100.) for i in range(12)])
    r_ramps = [[0., r1], [r1, r2], [r2, r3], [r3, r4],[r4, 0.]]
    g_ramps = [[0., g1], [g1, g2], [g2, g3], [g3, g4],[g4, 0.]]
    b_ramps = [[0., b1], [b1, b2], [b2, b3], [b3, b4],[b4, 0.]]


    for i in range(len(r_ramps)):
        start_point.set_x(make_color_ramp(canvas,
                                          start_point,
                                          r_ramps[i],
                                          g_ramps[i],
                                          b_ramps[i],
                                          n_steps,
                                          ramp_height))

    root.mainloop()
    
    
def make_color_ramp(
    canvas, start_point, r_ramp, g_ramp, b_ramp, n_steps, ramp_height):
    
    r_shift = get_color_shift(r_ramp, n_steps)
    g_shift = get_color_shift(g_ramp, n_steps)
    b_shift = get_color_shift(b_ramp, n_steps)

    for step in range(n_steps):
        r_val = get_ramp_val_at_step(r_ramp, r_shift, step)
        g_val = get_ramp_val_at_step(g_ramp, g_shift, step)
        b_val = get_ramp_val_at_step(b_ramp, b_shift, step)
        color = rgb2hex(r_val, g_val, b_val)
        canvas.create_line(start_point.x + step, start_point.y,
                           start_point.x + step, start_point.y + ramp_height,
                           fill=color,
                           width=1)

    return start_point.x + n_steps


def get_color_shift(ramp, n_steps):
    return (ramp[1] - ramp[0]) / n_steps


def get_ramp_val_at_step(ramp, shift, step):
    val = 2.55 * (ramp[0] + shift * step)
    if val > 255:
        val = 255.
    if val < 0:
        val = 0
    return val




if __name__ == '__main__':
    main()
