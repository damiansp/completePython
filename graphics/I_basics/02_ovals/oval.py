from tkinter import *

root = Tk()
root.title('Ellipse')

W, H = 700, 500
PAD = 50
canvas = Canvas(root, width=W, height=H, background='white')
canvas.grid(row=0, column=1)

bb = [[PAD, PAD], [W - PAD, H - PAD]]
canvas.create_oval(
    bb[0][0], bb[0][1], bb[1][0], bb[1][1],fill='black', outline='red', width=4)




root.mainloop()
