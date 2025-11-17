import tkinter as tk


class ClickApp(tk.Tk):
    """ Button clicker application """
    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()
        self.background_colour_frame = BackgroundColorFrame(self)
        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.clicker_frame.pack(side=tk.LEFT)
        self.background_colour_frame.pack(side=tk.RIGHT)




class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """
    def __init__(self, master):
        super().__init__(master)
        self.count = 0
        self.greeting = tk.Label(master, text='Welcome to COUNTY THINGY')
        self.greeting.pack(side=tk.TOP)
        self.clickee = tk.Button(master, text='Click me', fg='black', bg='ivory2', activebackground='ivory4',
                                 activeforeground='white',command=self.click_button)
        self.clickee.pack(side=tk.TOP)

        self.counter = tk.Label(master, text=f'{self.count} clicks')
        self.counter.pack(side=tk.TOP)

        self.dontclick = tk.Button(master, text='Do not press this button', fg='white', bg='red',
                                   activebackground='red4',
                                   activeforeground='white')
        self.dontclick.pack(side=tk.BOTTOM)

    def click_button(self):
        self.count += 1
        self.counter.config(text = f'{self.count} clicks')


class BackgroundColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # Color choices

        self.colors = ['red', 'green', 'yellow']

        # Create a tk variable which will hold the value of the selcted color
        #self.selected_color = self.colors[0]
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])
        self.config(bg = self.selected_color.get())

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color)
                              for color in self.colors]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        self.master.config(bg = self.selected_color.get())
        self.config(bg = self.selected_color.get())
        pass
        #self.configure(bg=str(self.selected_color))

if __name__ == '__main__':
    app = ClickApp()
    app.geometry('500x300')
    app.mainloop()