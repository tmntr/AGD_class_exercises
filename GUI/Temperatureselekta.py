import tkinter as tk

class TempApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.background_colour_frame = BackgroundColorFrame(self)

        self.background_colour_frame.pack(side=tk.RIGHT)

class TemperatureConvertingFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.units = ['Kelvin','Celsius','Fahrenheit']


        self.current_units = tk.StringVar()
        self.current_units.set(self.units[0])

        self.converted_units = tk.StringVar()
        self.converted_units.set(self.units[0])

        self.button = tk.Button(self, text='Random colour', command=self.calculate,
                                background='red',foreground='white',activebackground='cyan')


        self.current_units_options = [tk.Radiobutton(self, text=unit,
                                             value=unit,
                                             variable=self.current_units,
                                             )
                              for unit in self.units]

        self.converted_units_options = [tk.Radiobutton(self, text=unit,
                                                     value=unit,
                                                     variable=self.converted_units,
                                                     )
                                      for unit in self.units]


        self.place_widgets()

    def place_widgets(self):

        i = 0
        for item in self.current_units_options:
            item.grid(row=2, column=i)
            i += 1

        i = 0
        for item in self.converted_units_options:
            item.grid(row=2, column=i)
            i += 1


    def calculate(self):
        pass



if __name__ == '__main__':
    app = TempApp()
    app.geometry('500x300')
    app.mainloop()