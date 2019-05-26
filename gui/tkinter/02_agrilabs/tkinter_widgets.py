import tkinter as tk
from tkinter import ttk

my_entry = ttk.Entry(parent, textvariable=my_text_var)
my_spinbox = tk.Spinbox(
    parent, from_=0.5, to=52., increment=0.01, textvariable=my_double_var)
combo_box = ttk.Combobox(
    parent, textvariable=my_str_var, values=['Opt 1', 'Opt 2', 'Opt 3'])
