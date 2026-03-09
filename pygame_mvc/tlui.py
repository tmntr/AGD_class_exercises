from game_objects import *

thegame = Game()

thegame.set_background_from_file('background.txt')

thegame.set_up()

while True:
    for char in thegame.characters:
        thegame.textdisplay()
        direction = input("Please enter your direction (WASD): ")
        char.try_to_move(direction)
        for item in thegame.check_for_win():
            print(f"{item.name} wins!")