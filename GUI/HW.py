import tkinter as tk
from tkinter import ttk


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

        self.txt = tk.Label(self, text='Please complete this beautiful form',background='ivory3')

        self.nametxt = tk.Label(self, text='Name:',background='ivory2')
        self.name = tk.Entry(self)
        self.emailtxt = tk.Label(self, text='Email:',background='ivory2')
        self.email = tk.Entry(self)
        self.agetxt = tk.Label(self, text='Age:',background='ivory2')
        self.sld = tk.Scale(self, from_=0, to=100, length=200, orient=tk.HORIZONTAL,background='ivory2')

        self.genders = ['Male', 'Female', 'Other']

        self.gendertxt = tk.Label(self, text='Gender:',background='ivory2')

        self.selected_gender = tk.StringVar()
        self.selected_gender.set(self.genders[0])

        self.radio_options = [tk.Radiobutton(self, text=gender,
                                             value=gender,background = 'ivory2')
                              for gender in self.genders]
        self.codetxt = tk.Label(self, text='Coding languages:',background='ivory2')

        self.checkbox_options = [tk.Checkbutton(self, text=item, onvalue=1, offvalue=0,background = 'ivory2') for item in
                                 ["python", "javascript"]]


        self.countrytxt = tk.Label(self, text='Country:',background='ivory2')
        self.countrybox = ttk.Combobox(self,width = 30)
        self.countrybox['values'] = ['Jamiaca',
                                     'UK',
                                     'Taiwan',
                                     'Ireland',
                                     'India',
                                     'New Zealand',
                                     'South Korea',
                                     'Uganda',
                                     'The Unconvincing States of North America',
                                     'Lichtenstein',
                                     'Switzerland',
                                     'Middle Earth',
                                     ]


        self.submitbutton = tk.Button(self, text='Submit', foreground='black', background='ivory4',
                                      activebackground='blue', activeforeground='white', width=6)
        self.config(bg='ivory2')

        self.place_widgets()

    def place_widgets(self):
        self.txt.grid(row=0, column=0, columnspan=2)
        self.nametxt.grid(row=1, column=0)
        self.name.grid(row=1, column=1)
        self.emailtxt.grid(row=2, column=0)
        self.email.grid(row=2, column=1)
        self.agetxt.grid(row=3, column=0)
        self.sld.grid(row=3, column=1)

        self.submitbutton.grid(row=7, column=1, columnspan=3)
        self.gendertxt.grid(row=4, column=0)

        i = 1
        for ro in self.radio_options:
            ro.grid(row=4, column=i, padx=(5, 10), pady=5)
            i += 1

        self.codetxt.grid(row=5, column=0)

        j = 1
        for co in self.checkbox_options:
            co.grid(row=5, column=j, padx=(5, 10), pady=5)
            j += 1
        self.countrytxt.grid(row=6, column=0)
        self.countrybox.grid(row=6, column=1)

if __name__ == '__main__':
    mainframe = MainApp()
    mainframe.title('Tom\'s epic and most bodacious TKINTER THING!!!!')
    mainframe.grid()
    mainframe.mainloop()


# if btn.press
