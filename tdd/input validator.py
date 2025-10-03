import pyinputplus as pyip

name = pyip.inputStr('What is your name?\n')



age = pyip.inputInt('How old are you?\n',
                    min=3,
                    max=100
                    )

