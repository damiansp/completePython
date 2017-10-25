import sys
from tkinter import *

sys.path.append('../../')
from util import hex2rgb, Point


def main():
    root = Tk()
    root.title('Color Transititions along a Gradient')

    W, H = 300, 750
    PAD = 8
    canvas = Canvas(root, width=W, height=H, background='black')
    canvas.grid(row=0, column=1)

    fonts = ['Bookantiqua 12 bold', 'Bookantiqua 10 bold']
    start_color = '#ff0000'
    end_color   = '#ffff00'
    swatch_start = Point(20, 10)
    swatch_width = 40
    swatch_height = 40
    n_steps = 8

    colors = make_discrete_color_series(start_color, end_color, n_steps)
    for i in range(n_steps):
        show_swatch(canvas,
                    colors[i],
                    swatch_start,
                    swatch_width,
                    swatch_height,
                    PAD,
                    fonts)
        swatch_start.set_y(swatch_start.y + swatch_height + PAD)

    root.mainloop()


def make_discrete_color_series(start_color, end_color, n_steps):
    '''Expects start and end as hex strings'''
    start_color, end_color = hex2rgb(start_color), hex2rgb(end_color)

    # deltas
    dr = (end_color[0] - start_color[0]) / (n_steps - 1)
    dg = (end_color[1] - start_color[1]) / (n_steps - 1)
    db = (end_color[2] - start_color[2]) / (n_steps - 1)

    #color_series_int = []
    color_series_hex = []

    for i in range(n_steps + 1):
        r = get_color_at_step(start_color[0], dr, i)
        g = get_color_at_step(start_color[1], dg, i)
        b = get_color_at_step(start_color[2], db, i)
        #color_series_int.append((r, g, b))
        
        if i < n_steps:
            color_series_hex.append('#%02x%02x%02x' % (r, g, b))
        else:
            color_series_hex.append('#%02x%02x%02x' % end_color)

    return color_series_hex



def get_color_at_step(start_color, delta, step):
    color = start_color + step * delta
    color = color if color > 0 else 0
    color = color if color < 255 else 255
    return int(color)


def show_swatch(canvas, color_hex, start_point, width, height, pad, fonts):
    TEXT_PAD = 10
    TEXT_WIDTH = 200
    panel = (start_point.as_list(),
             (start_point + Point(width, height)).as_list())
    canvas.create_rectangle(panel, fill=color_hex)
    start_point.set_y(start_point.y + height + pad)
    canvas.create_text(
        (start_point + Point(width + TEXT_PAD, -height - TEXT_PAD)).as_list(),
        text=color_hex,
        fill=color_hex,
        width=TEXT_WIDTH,
        anchor=NW,
        font=fonts[0])

    color_int = hex2rgb(color_hex)
    canvas.create_text(
        (start_point + Point(width + TEXT_PAD, -height + TEXT_PAD)).as_list(),
        text=color_int,
        fill=color_hex,
        width=TEXT_WIDTH,
        anchor=NW,
        font=fonts[1])
    

if __name__ == '__main__':
    main()
