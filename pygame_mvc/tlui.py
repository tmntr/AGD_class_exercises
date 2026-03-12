from game_objects import *

'''class arbitraryTUI:
    def __init__(self,filename):
        self.thegame = Game()
    def initialisegame(self):
        self.thegame = Game()'''


thegame = Game()

thegame.set_background_from_file('background.txt')

noplayers = int(input('How many players would you like?\n'))

for i in range(noplayers):
    thegame.set_up('Carl')


while not len(thegame.check_for_win()):
    for char in thegame.characters:
        thegame.textdisplay()
        print(f'{char.name}\'s turn')
        direction = input("Please enter your direction (WASD): ").upper()
        char.try_to_move(direction)
for item in thegame.check_for_win():
    print(f"{item.name} wins!")