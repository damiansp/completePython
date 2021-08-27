import sys
from tkinter import *

sys.path.append('../../')
from util import

def main():
    root = Tk()
    root.title('')

    W, H = 700, 500
    canvas = Canvas(root, width=W, height=H, background='white')
    canvas.grid(row=0, column=1)

    
    root.mainloop()




if __name__ == '__main__':
    main()
