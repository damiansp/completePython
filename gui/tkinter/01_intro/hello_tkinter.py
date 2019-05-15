from tkinter import *
from tkinter.ttk import *


root = Tk()
label = Label(root, text='Hello, World!')
label.pack()
text = Entry()
text.pack()
button = Button(root, text='Click Me!')
button.pack()
bye_label = Label(root, text='Bye Bye!')
bye_label.pack()
root.mainloop()

print('you must have closed the application')
