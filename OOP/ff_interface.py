import time
from colorama import Fore,Back,Style
from fighting_fantasy import Character, PlayerCharacter, Game

def cooltype(text='Rian',interval=0.01,nextline = True):
    for item in text:
        print(item,end='')
        time.sleep(interval)
    if nextline:
        print('\n')
def cooltypecolour(text='Rian',interval=0.05,colour=Fore.MAGENTA,nextline = True):
    print(colour)
    cooltype(text,0.05)
    print(Style.RESET_ALL)
    if nextline:
        print('\n')
def coolinput(text='',interval=0.01):
    for item in text:
        print(item,end='')
        time.sleep(interval)
    return input()



class gamedisplay:
    def __init__(self):
        self.game = Game()

    def game_setup(self):
        name = coolinput("What is your name? ")
        Bim = PlayerCharacter.generate_player_character(name)
        cooltype(Bim.return_character_status())
        self.game.player = Bim
    def battle_setup(self):
        self.game.choose_opponent()
        cooltype(f"You, {self.game.player.name}, have been pitted against {self.game.op.name}.")
        cooltype(self.game.player.return_character_status())
        cooltype(self.game.op.return_character_status())

        cooltype("Good Luck.\n\n")
    def battle(self):
        fleeing = False
        while self.game.continue_fighting() and not fleeing:
            self.game.resolve_fight_round()
            cooltype(self.game.return_round_result())
            if not self.game.player.is_dead:
                accepted = False
                while not accepted:
                    accepted = True
                    action = coolinput("\n^ Would you like to fight again? (y/n) ^ ")
                    if action == "y":
                        pass
                    elif action == "n":
                        cooltype('You attempt to flee',0.01,False)
                        cooltype('...',0.1)

                        if self.game.attempt_flee():
                            cooltype('You live to fight another day!')
                            fleeing = True
                        else:
                            cooltypecolour((f'{self.game.op.name} is too good, and catches you as you leave' + '\b'*len(f'{self.game.op.name} is too good, and catches you as you leave')),0.01,Fore.RED)
                    else:
                        cooltypecolour(('Please enter y or n.' + '\b'*len('Please enter y or n.')),0.01,Fore.RED)
                        accepted = False
        if self.game.player.is_dead:
            cooltype(f'{self.game.player.name} was tragically slain by the mighty and terrible {self.game.op.name}')
        elif self.game.op.is_dead:
            cooltype(f'You are, of course, victorious, and have slain {self.game.op.name}!')
        else:
            cooltype(f'You decided that {self.game.op.name} was not worth your time.')

gameCLI = gamedisplay()

gameCLI.game_setup()
running = True
while running:
    gameCLI.battle_setup()
    gameCLI.battle()
    decision = input("Do you want to play again? (y/n)\n")
    if decision == "n":
        cooltype('Are you sure? (y/n/)\n')
        decision = input()
        if decision == "n":

    elif decision == "y":
        pass
    else:
        cooltype("I'll take that as a yes!")



