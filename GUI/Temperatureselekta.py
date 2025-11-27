import tkinter as tk
import temperature as temp

class TempApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.background_colour_frame = TemperatureConvertingFrame(self)

        self.background_colour_frame.pack(side=tk.BOTTOM)

class TemperatureConvertingFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.og_temperature =temp.Temperature(0)

        self.og_text_temp = tk.StringVar()

        self.og_temperature_box = tk.Entry(self,textvariable=self.og_text_temp,width = 20)

        self.og_units = UnitsFrame(self)

        self.og_selected_unit = self.og_units.selected_unit

        self.conv_temperature = temp.Temperature(0)

        self.temporarytemperature = tk.IntVar()

        self.devslider = tk.Scale(self,variable =self.temporarytemperature,from_=0, to=1000, length=400, command=self.updatecolour)

        self.conv_text_temp = tk.StringVar()

        self.conv_temperature_box = tk.Label(self, text=self.conv_text_temp.get(),background = 'white',width = 20)

        self.conv_units = UnitsFrame(self)

        self.submit_button = tk.Button(self,background='cyan',foreground='blue',activebackground='blue',activeforeground='white',width = 20,text = 'CONVERT')

        self.place_widgets()

    def updatecolour(self, temp):
        self.config(background=self.get_current_colour(int(temp)))

    def place_widgets(self):
        settings = {'padx':10,'pady':10}


        self.og_temperature_box.grid(row=0, column=0,sticky = 'w',**settings)
        self.conv_temperature_box.grid(row=0, column=1, sticky='e',**settings)
        self.submit_button.grid(row=1,column=0,sticky='n',columnspan=2,**settings)
        self.og_units.grid(row=2, column=0, sticky='w',**settings)
        self.conv_units.grid(row = 2, column = 1, sticky = 'e',**settings)
        self.devslider.grid(row = 3, column=0, sticky = 'w',**settings)

    def from_rgb(self,rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb


    def get_current_colour(self,quantity):
        if quantity < 273:
            colour = (0,0,quantity/273*255)
        elif quantity < 373:
            colour = ((quantity-273)/100*255,0,255-(quantity-273)/100*255)
        elif quantity < 1273:
            colour = (255,(quantity-273)/1000*255,(quantity-273)/1000*255)
        else:
            colour = (255,255,255)

        print(colour)
        colourforuse = (int(colour[0]),int(colour[1]),int(colour[2]))
        return self.from_rgb(colourforuse)



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