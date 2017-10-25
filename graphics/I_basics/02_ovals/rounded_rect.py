from tkinter import *

root = Tk()
root.title('')

W, H = 700, 500
PAD = 20
canvas = Canvas(root, width=W, height=H, background='white')

canvas.grid(row=0, column=1)

def rounded_rect(
    canvas, upper_left, bottom_right, percent, outline_color='black', width=1):
    
    x1, y1 = upper_left
    x2, y2 = bottom_right
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    hc = int(round(h * percent))
    wc = int(round(w * percent))

    # straight parts
    canvas.create_line(x1 + wc, y1,
                       x2 - wc, y1,
                       fill=outline_color,
                       width=width)
    canvas.create_line(x1 + wc, y2,
                       x2 - wc, y2,
                       fill=outline_color,
                       width=width)
    canvas.create_line(x1, y1 + hc,
                       x1, y2 - hc,
                       fill=outline_color,
                       width=width)
    canvas.create_line(x2, y1 + hc,
                       x2, y2 - hc,
                       fill=outline_color,
                       width=width)

    # arcs
    # ur:
    bb = x2 - 2*wc, y1, x2, y1 + 2*hc
    dx = w - 2*wc
    dy = h - 2*hc
    canvas.create_arc(
        bb, start=0, extent=90, style=ARC, outline=outline_color, width=width)
    # ul
    bb = bb[0] - dx, bb[1], bb[2] - dx, bb[3]
    canvas.create_arc(
        bb, start=90, extent=90, style=ARC, outline=outline_color, width=width)
    # bl
    bb = bb[0], bb[1] + dy, bb[2], bb[3] + dy
    canvas.create_arc(
        bb, start=180, extent=90, style=ARC, outline=outline_color, width=width)
    # br
    bb = bb[0] + dx, bb[1], bb[2] + dx, bb[3]
    canvas.create_arc(
        bb, start=270, extent=90, style=ARC, outline=outline_color, width=width)
    
upper_left = PAD, PAD
bottom_right = W - PAD, H - PAD
width = 10

for i in range(width):
    rounded_rect(canvas,
                 upper_left,
                 bottom_right,
                 percent=0.4,
                 outline_color='red',
                 width=2 * width)

    upper_left = upper_left[0] + PAD, upper_left[1] + PAD
    bottom_right = bottom_right[0] - PAD, bottom_right[1] - PAD
    width -= 1
    

root.mainloop()
