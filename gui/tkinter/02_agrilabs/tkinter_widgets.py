import tkinter as tk
from tkinter import ttk

my_entry = ttk.Entry(parent, textvariable=my_text_var)
my_spinbox = tk.Spinbox(
    parent, from_=0.5, to=52., increment=0.01, textvariable=my_double_var)
combo_box = ttk.Combobox(
    parent, textvariable=my_str_var, values=['Opt 1', 'Opt 2', 'Opt 3'])
my_checkbutton = ttk.Checkbutton(
    parent, text='Pick Me!', variable=my_boolean_var)

# Creating a Text widget
my_text = tk.Text(parent)
my_text.insert('1.0', 'I love my text widget!')
my_text.insert('1.2', 'REALLY ')
my_text.get('1.0', tk.END)
my_text.delete('end - 2 chars') # removes "!\n"
