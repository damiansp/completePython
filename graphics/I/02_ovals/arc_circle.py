from tkinter import *

root = Tk()
root.title('Arc Circle')

W, H = 500, 500
PAD = 50
canvas = Canvas(root, width=W, height=H, background='white')

canvas.grid(row=0, column=1)

bb = PAD, PAD, W - PAD, H - PAD

canvas.create_arc(bb, start=0, extent=359.9999, fill='cyan')
root.mainloop()
