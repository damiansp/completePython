from datetime import datetime
import tkinter as tk
from tkinter import tkk

from . import widgets as w


class DataRecordForm(tk.Frame):
    '''The input form for the widgets'''
    def __init__(self, parent, fields, *args, **kwargs):
	      super().__init__(parent, *args, **kwargs)
        self.inputs = {}

        record_info = tk.LabelFrame(self, text='Record Information')
        self.inputs['Date'] = w.LabelInput(record_info,
                                           'Date',
                                           field_spec=fields['Date'])
        self.inputs['Date'].grid(row=0, column=0)
        self.inputs['Time'] = w.LabelInput(record_info,
                                           'Time',
                                           field_spec=fields['Time'])
        self.inputs['Time'].grid(row=0, column=1)
        self.inputs['Technician'] = w.LabelInput(
            record_info,
            'Technician',
            field_spec=fields['Technician'])
        self.inputs['Technician'].grid(row=0, column=2)
        self.inputs['Lab'] = w.LabelInput(record_info,
                                          'Lab',
                                          field_spec=fields['Lab']
	      self.inputs['Lab'].grid(row=1, column=0)
        self.inputs['Plot'] = LabelInput(record_info,
	                                       'Plot',
                                         field_spec=fields['Plot'])
        self.inputs['Plot'].grid(row=1, column=1)
	      self.inputs['Seed sample'] = w.LabelInput(
            record_info, 'Seed sample', input_var=tk.StringVar())
        self.inputs['Seed sample'].grid(row=1, column=2)
	      record_info.grid(row=0, column=0, sticky=tk.W + tk.E)

        environment_info = tk.LabelFrame(self, text='Environment Data')
        self.inputs['Humidity'] = LabelInput(environment_info,
                                             'Humidity (g/m^3)',
                                             field_spec=fields['Humidity'])
        self.inputs['Humidity'].grid(row=0, column=0)
        self.inputs['Light'] = w.LabelInput(environment_info,
	                                          'Light (klx)',
                                            field_spec=fields['Light'])
        self.inputs['Light'].grid(row=0, column=1)
        self.inputs['Temperature'] = w.LabelInput(
            environment_info,
            'Temperature (C)',
            field_spec=fields['Temperature'])
        self.inputs['Temperature'].grid(row=0, column=2)
        self.inputs['Equipment Fault'] = w.LabelInput(
            environment_info,
            'Equipment Fault',
            field_spec=fields['Equipment Fault'])
        self.inputs['Equipment Fault'].grid(row=1, column=0, columnspan=3)
        environment_info.grid(row=1, column=0, sticky=tk.W + tk.E)

        plant_info = tk.LabelFrame(self, text='Plant Data')
        self.inputs['Plants'] = w.LabelInput(plant_info,
                                             'Plants',
                                             field_spec=fields['Plants'])
        self.inputs['Plants'].grid(row=0, column=0)
        self.inputs['Blossoms'] = w.LabelInput(plant_info,
                                               'Blossoms',
                                               field_spec=fields['Blossoms'])
        self.inputs['Blossoms'].grid(row=0, column=1)
        self.inputs['Fruit'] = w.LabelInput(plant_info,
                                            'Fruit',
                                            field_spec=fields['Fruit'])
        self.inputs['Fruit'].grid(row=0, column=2)
        min_height_var = tk.DoubleVar(value='-infinity')
        max_height_var = tk.DoubleVar(value='infinity')
        self.inputs['MinHeight'] = w.LabelInput(
            plant_info,
            'Min Height (cm)',
            field_spec=fields['MinHeight'],
            input_class=w.ValidatedSpinbox,
            input_args={'max_var': max_height_var,
                        'focus_update_var': min_height_var})
        self.inputs['MinHeight'].grid(row=1, column=0)
        self.inputs['MaxHeight'] = w.LabelInput(
            plant_info,
            'Max Height (cm)',
            field_spec=fields['MaxHeight'],
            input_args={'min_var': min_height_var,
                        'focus_update_var': max_height_var})
        self.inputs['MaxHeight'].grid(row=1, column=1)
        self.inputs['MedianHeight'] = w.LabelInput(
            plant_info,
            'Median Height (cm)',
            field_spec=fields['MedianHeight'],
            input_args={'min_var': min_height_var,
                        'max_var': max_height_var})
        self.inputs['MedianHeight'].grid(row=1, column=2)
        self.inputs['Notes'] = w.LabelInput(self,
                                            'Notes',
                                            field_spec=fields['Notes'])
                                            #input_args={'width': 75,
                                            #            'height': 10})
        self.inputs['Notes'].grid(sticky='w', row=3, column=0)
        plant_info.grid(row=2, column=0, sticky=tk.W + tk.E)
        self.reset()

    def get(self):
        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        '''Reset the form entries'''
        lab = self.inputs['Lab'].get()
        time = self.inputs['Time'].get()
        technician = self.inputs['Technician'].get()
        plot = self.inputs['Plot'].get()
        plot_values = self.inputs['Plot'].input.cget('values')
        for widget in self.inputs.values():
            widget.set('')
        current_date = datetime.today().strftime('%Y-%m-%d')
        self.inputs['Date'].set(current_date)
        self.inputs['Time'].input.focus()
        #self.inputs['Time'].set(time)                                           
        if plot not in ('', plot_values[-1]):
            self.inputs['Lab'].set(lab)
            slef.inputs['Time'].set(time)
            self.inputs['Technician'].set(technician)
            next_plot_index = plot_values.index(plot) + 1
            self.inputs['Plot'].set(plot_values[next_plot_index])
            self.inputs['Seed sample'].input.focus()

    def get_errors(self):
        '''Get a list of field errors in the form'''
        errors = {}
        for key, widget in self.inputs.items():
            if hasattr(widget.input, 'trigger_focusout_validation'):
                widget.input.trigger_focusout_validation()
            if widget.error.get():
                errors[key] = widget.error.get()
        return errors
