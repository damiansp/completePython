from tkinter import *

root = Tk()
root.title('Named Colors')

W, H = 700, 500
PAD = 20
canvas = Canvas(root, width=W, height=H, background='white')

canvas.grid(row=0, column=1)

reds = ['orange red', 'red', 'IndianRed1', 'firebrick1', 'red4']
yellows = ['yellow', 'gold', 'orange', 'DarkOrange3']
blues = ['sky blue', 'steel blue', 'dodger blue', 'blue', 'blue4',
         'midnight blue', 'royal blue', 'RoyalBlue4']

x1, y1 = PAD, PAD
width = (W - 4*PAD) / 3
height = (H - 9*PAD) / 8

text_offset = 0
text_width = 90
swatch = [x1, y1, x1 + width, y1 + height]

def show_color_set(c_set):
    for i in range(len(c_set)):
        canvas.create_rectangle(swatch, fill=c_set[i])
        canvas.create_text(swatch[0] + width / 4, swatch[1] + height / 4,
                           text=c_set[i],
                           width=text_width,
                           anchor=NW)

        swatch[1] += PAD + height
        swatch[3] += PAD + height

color_sets = [reds, yellows, blues]

for i in range(3):
    show_color_set(color_sets[i])

    swatch[0] += PAD + width
    swatch[1] = y1
    swatch[2] += PAD + width
    swatch[3] = y1 + height

root.mainloop()
