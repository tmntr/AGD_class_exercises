import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self, text = 'Welcome to Tom\'s epic and most bodacious TKINTER THING!!!!')


        self.btn = tk.Button(root, text = 'Do not press this button', fg = 'white', bg='red', activebackground= 'red4',activeforeground= 'white')
        self.btn2 = tk.Button(root, text='Do not press this button either', fg='white', bg='blue', activebackground='blue4',
                             activeforeground='white')
        self.edt = tk.Entry(self)
        self.sld = tk.Scale(self, from_=0, to=2000, orient=tk.VERTICAL)
        self.config(bg='ivory2')
        self.place_widgets()

    def place_widgets(self):
        settings = {'padx':10, 'pady':10,'sticky':'nswe'}
        self.txt.grid(row=0, column=0, **settings)
        self.btn.grid(row=0, column=0, **settings)
        self.btn2.grid(row=0, column=1, **settings)
        self.edt.grid(row=1, column=0, **settings)
        self.sld.grid(row=2, column=0, **settings)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500+100+100')
    root.title('Tom\'s epic and most bodacious TKINTER THING!!!!')
    mainframe = MainFrame(root)
    mainframe.grid()
    root.mainloop()
    #if btn.press