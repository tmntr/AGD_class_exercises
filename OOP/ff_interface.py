
from fighting_fantasy import Character, PlayerCharacter, Game

class gamedisplay:
    def __init__(self):
        self.game = Game()

    def game_setup(self):
        name = input("What is your name? ")
        Bim = PlayerCharacter.generate_player_character(name)
        print(Bim.return_character_status())
        self.game.player = Bim
    def battle_setup(self):
        self.game.choose_opponent()
        print(f"You, {self.game.player.name}, have been pitted against {self.game}.")
        print("Good Luck.")
    def battle(self):
        while self.game.continue()
        self.game.battle(self.game.op)
