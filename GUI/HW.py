import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()
        self.Form_frame = FormFrame(self)
        self.geometry('400x300')

        self.title('Click Counter')

        self.Form_frame.pack(side=tk.LEFT)

class FormFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self, text = 'Please complete this form')

        self.nametxt = tk.Label(self, text='Name:')
        self.name = tk.Entry(self)
        self.emailtxt = tk.Label(self, text='Email:')
        self.email = tk.Entry(self)
        self.agetxt = tk.Label(self, text='Age:')
        self.sld = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.submitbutton = tk.Button(self, text='Submit', foreground='black', background='ivory4',
                                      activebackground='blue', activeforeground='black',width=2)
        self.config(bg='ivory2')

        self.genders = ['Male', 'Female', 'Other']

        self.selected_gender = tk.StringVar()
        self.selected_gender.set(self.genders[0])

        self.radio_options = [tk.Radiobutton(self, text=gender,
                                             value=gender, )
                              for gender in self.genders]

        self.place_widgets()



        self.place_widgets()



    def place_widgets(self):
        self.txt.grid(row=0, column=0, columnspan=2)
        self.nametxt.grid(row=1, column=0)
        self.name.grid(row=1, column=1)
        self.emailtxt.grid(row=2, column=0)
        self.email.grid(row=2, column=1)
        self.agetxt.grid(row=3, column=0)
        self.sld.grid(row=3, column=1)
        self.submitbutton.grid(row=5, column=2,columnspan=2)
        i = 1
        for ro in self.radio_options:
            ro.grid(row = 4,column = i, padx=(5, 10), pady=5)
            i += 1


if __name__ == '__main__':
    mainframe = MainApp()
    mainframe.title('Tom\'s epic and most bodacious TKINTER THING!!!!')
    mainframe.grid()
    mainframe.mainloop()
    #if btn.press