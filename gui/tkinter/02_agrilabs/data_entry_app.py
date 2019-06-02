import tkinter as tk
from tkinter import ttk


class LabelInput(tk.Frame):
    '''A widget containing a label and input together.'''
    def __init__(
            self, parent, label='', input_class=tkk.Entry, input_var=None,
            input_args=None, label_args=None, **kwargs):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var
        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
            input_args['text'] = label
            input_args['variable'] = input_var
        else:
            self.label = ttk.Label(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
            input_args['textvariable'] = input_var
        self.input = input_class(self, **input_args)
        self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        super().grid(sticky=sticky, **kwargs)

    def get(self):
        try:
            if self.variable:
                return self.variable.get()
            elif type(self.input) == tk.Text:
                return self.input.get('1.0', tk.END)
            else:
                return self.input.get()
        except (TypeError, tk.TclError): # if numeric fields are empty
            return ''

    def set(self, value, *args, **kwargs):
        if type(self.variable) == tk.BooleanVar:
            self.variable.set(bool(value))
        elif self.variable:
            self.variable.set(value, *args, **kwargs)
        elif type(self.input) in (ttk.Checkbutton, ttk.Radiobutton):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else: # input mush be an Entry-type widget with no variable
            self.input.delete(0, tk.END)
            self.input.insert(0, value)
        

class DataRecordForm(tk.Frame):
    '''The input form for the widgets'''
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.inputs = {}
        record_info = tk.LabelFrame(self, text='Record Information')
        self.inputs['Date'] = LabelInput(
            record_info, 'Date', input_var=tk.StringVar())
        self.inputs['Date'].grid(row=0, column=0)
        self.inputs['Time'] = LabelInput(
            record_info,
            'Time',
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={'values': ['8:00', '12:00', '16:00', '20:00']})
        self.inputs['Time'].grid(row=0, column=1)
        self.inputs['Technician'] = LabelInput(
            record_info, 'Technician', input_var=tk.StringVar())
        self.inputs['Tecnician'].grid(row=0, column=2)
        self.inputs['Lab'] = LabelInput(
            record_info,
            'Lab',
            input_class=ttk.Combobox,
            input_var=tk.StringVar(),
            input_args={'values': ['A', 'B', 'C', 'D', 'E']})
        self.inputs['Lab'].grid(row=1, column=0)
        self.inputs['Plot'] = LabelInput(
            record_info,
            'Plot',
            input_class=ttk.Combobox,
            input_var=tk.IntVar(),
            input_args={'values': list(range(1, 21))})
        self.inputs['Plot'].grid(row=1, column=1)
        self.inputs['Seed sample'] = LableInput(
            record_info, 'Seed sample', input_var=tk.StringVar())
        self.inputs['Seed sample'].grid(row=1, column=2)
        record_info.grid(row=0, column=0, sticky=tk.W + tk.E)
        environment_info = tk.LabelFrame(self, text='Environment Data')
        self.inputs['Humidity'] = LabelInput(
            environment_info,
            'Humidity (g/m^3)',
            input_class=tk.Spinbox,
            input_var=tk.DoubleVar(),
            input_args={'from_': 0.5, 'to': 52., 'increment': 0.01})
        self.inputs['Humidity'].grid(row=0, column=0)
        # CONTINUE HERE...

    
class Application(tk.Tk):
    '''Application root window'''


if __name__ == '__main__':
    app = Application()
    app.mainloop()
