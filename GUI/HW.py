import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self, text = 'I cannot quite remember the assignment, but here are some ')



        self.edt = tk.Entry(self)
        self.sld = tk.Scale(self, from_=0, to=2000, orient=tk.VERTICAL)
        self.config(bg='ivory2')
        self.place_widgets()

    def place_widgets(self):
        self.txt.grid(row=0, column=0)
        self.edt.grid(row=1, column=0)
        self.sld.grid(row=10, column=0)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tom\'s epic and most bodacious TKINTER THING!!!!')
    mainframe = MainFrame(root)
    mainframe.grid()
    root.mainloop()
    #if btn.press