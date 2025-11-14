import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self, text = '''I cannot quite remember the assignment,
                                         but here are some of the bits I remember being in it''')

        self.nametxt = tk.Label(self, text='Name:')
        self.name = tk.Entry(self)
        self.agetxt = tk.Label(self, text='Age:')
        self.sld = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.submitbutton = tk.Button(self, text='Submit', foreground='black', background='ivory4',
                                      activebackground='blue', activeforeground='white',width=2)
        self.config(bg='ivory2')
        self.place_widgets()


    def place_widgets(self):
        self.txt.grid(row=0, column=0, columnspan=2)
        self.nametxt.grid(row=1, column=0)
        self.name.grid(row=1, column=1)
        self.agetxt.grid(row=2, column=0)
        self.sld.grid(row=2, column=1)
        self.submitbutton.grid(row=3, column=2,columnspan=2)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tom\'s epic and most bodacious TKINTER THING!!!!')
    mainframe = MainFrame(root)
    mainframe.grid()
    root.mainloop()
    #if btn.press