from tkinter import *

root = Tk()
root.title('')

W, H = 700, 500
PAD = 50
canvas = Canvas(root, width=W, height=H, background='black')

canvas.grid(row=0, column=1)

x1, y1 = PAD, PAD
width, height = W - 2 * PAD, (H - 2 * PAD) / 4
text_offset = 0
text_width = 90
block = [x1, y1, x1 + width, y1 + height]
swatches = ['red', 'yellow', 'blue', 'green']

for i in range(4):
    canvas.create_rectangle(block, fill=swatches[i])
    canvas.create_text(block[0] + PAD, block[1] + height / 4,
                       text=swatches[i],
                       width=text_width,
                       fill=swatches[3 - i],
                       anchor=NW)

    block[1] += height
    block[3] += height

root.mainloop()
