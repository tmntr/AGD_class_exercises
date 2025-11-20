import tkinter as tk

class TempApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.background_colour_frame = TemperatureConvertingFrame(self)

        self.background_colour_frame.pack(side=tk.BOTTOM)

class TemperatureConvertingFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.og_temperature = tk.StringVar()
        self.og_temperature_box = tk.Entry(self,textvariable = self.og_temperature)

        self.og_units = UnitsFrame(self)

        self.og_selected_unit = self.og_units.selected_unit

        self.conv_temperature = tk.StringVar()
        self.conv_temperature_box = tk.Entry(self, textvariable=self.og_temperature)

        self.conv_units = UnitsFrame(self)

        self.place_widgets()

    def place_widgets(self):

        self.og_temperature_box.grid(row=0, column=0,sticky = 'w')
        self.conv_temperature_box.grid(row=0, column=1, sticky='e')
        self.submitbutton.grid(row=1)
        self.og_units.grid(row=2, column=0, sticky='w')
        self.conv_units.grid(row = 2, column = 1, sticky = 'e')


    def calculate(self):
        pass

class UnitsFrame(tk.Frame):
    def __init__(self, master,colour = 'Red'):
        super().__init__(master)
        self.master = master

        self.units = ['Kelvin','Celsius','Fahrenheit']

        self.selected_unit = tk.StringVar()
        self.selected_unit.set(self.units[0])





        self.units_options = [tk.Radiobutton(self, text=unit,
                                             value=unit,
                                             variable=self.selected_unit,background=colour
                                             )
                              for unit in self.units]

        self.place_widgets()

    def place_widgets(self):
        i = 0
        for unit in self.units_options:
            unit.grid(column=i, row=0)
            i+=1


if __name__ == '__main__':
    app = TempApp()
    app.geometry('500x300')
    app.mainloop()