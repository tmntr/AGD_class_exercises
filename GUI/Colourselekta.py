import tkinter as tk
import random

class ClickApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.background_colour_frame = BackgroundColorFrame(self)

        self.background_colour_frame.pack(side=tk.RIGHT)

class BackgroundColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # Color choices

        self.colors = ['red', 'yellow','green','blue','magenta','cyan','orange','pink','purple']


        # Create a tk variable which will hold the value of the selcted color
        #self.selected_color = self.colors[0]
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])
        self.config(bg = self.selected_color.get())
        self.master.config(background=self.selected_color.get())

        self.button = tk.Button(self, text='Random colour', command=self.randomcolour,
                                background=self.selected_color.get(),activebackground=random.choice(self.colors))
        self.button.pack(side=tk.BOTTOM)

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color,background=self.selected_color.get(),activebackground=color)
                              for color in self.colors]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)

    def change_color(self):
        self.master.config(bg = self.selected_color.get())
        self.config(bg = self.selected_color.get())
        self.button.config(bg = self.selected_color.get(),activebackground=random.choice(self.colors))
        for item in self.radio_options:
            item.config(background=self.selected_color.get())
        pass
        #self.configure(bg=str(self.selected_color))
    def randomcolour(self):
        self.selected_color.set(self.colors[random.randint(0,len(self.colors)-1)])
        self.change_color()

if __name__ == '__main__':
    app = ClickApp()
    app.geometry('500x300')
    app.mainloop()