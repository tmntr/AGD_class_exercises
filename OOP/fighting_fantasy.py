import random
from enum import nonmember

def dice_sum(num: int = 1,sides: int = 6):
    '''Indeedeth doth this procedure most chance-reliant return the grand total
    of all of a specified number of dice of a specified number of sides.'''
    dice_total = sum(random.randint(1, sides) for i in range(num))
    return dice_total


class Game:
    def __init__(self):
        self.opponent = None
        self.player = None
        self.creatures = self.loadcreatures()
        self.round_result = None

    def loadcreatures(cls):
        creatures = [
                    Character('orc', skill=5, stamina=12),
                    Character('dragon', skill=8, stamina=15)
                ]
        return creatures

    def resolve_fight_round(self):
        self.round_result = self.player.fight_round(self.opponent)

    def choose_opponent(self):
        self.opponent = random.choice(self.creatures)

    def battle(self,p1,p2):
        while not(self.player.is_dead or p2.is_dead):
            print(self.player.stamina, p2.stamina)
            self.player.fight_round(p2)
        if self.player.stamina > p2.stamina:
            print(f"{self.player.name} wins!")
        elif p2.stamina > p1.stamina:
            print(f"{p2.name} wins.")
            print("Game Over")
        else:
            print("A draw.")

class Character:
    def __init__(self,name,skill,stamina):
        self.name = name
        self.skill = skill
        self.defaultstamina = stamina
        self.stamina = self.defaultstamina*1
        self.roll = None
        self.score = None
    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"
    def __str__(self):
        return f"{self.name}"
    def find_score(self):
        self.roll = dice_sum()
        self.score = self.roll+self.skill

    def return_character_status(self):
        return f'{self.name} has skill {self.skill} and stamina {self.stamina}'

    def return_roll_status(self):
        return f'{self.name} rolled {self.roll} for a total score of {self.score}'

    def take_hit(self,damage = 2):
        self.stamina -= damage

    def fight_round(self,op):
        self.find_score()
        op.find_score()

        win = None

        if self.score < op.score:
            self.take_hit()
            win = 'lost'
        elif self.score > op.score:
            op.take_hit()
            win = 'win'
        else:
            self.take_hit(1)
            op.take_hit(1)
            win = 'draw'

        return win

    def return_rolls_status(self):
        return(f"{self.name} rolled a {self.roll} for a total score of {self.score}")

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self,dead:bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina,1)

    def reset_stamina(self):
        self.stamina = self.defaultstamina*1

class PlayerCharacter(Character):
    def __init__(self,name,skill,stamina,luck):
        super().__init__(name,skill,stamina)
        self.luck = luck
    def test_luck(self):
        self.luck -= 1
        diceroll = dice_sum(2)
        self.roll = diceroll
        if diceroll <= self.luck:
            return True
        else:
            return False
    def __repr__(self):
        return f"PlayerCharacter('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"

    @classmethod
    def generate_player_character(cls,name):
        skill = 6 + dice_sum(1,6)
        stamina = 12+dice_sum(2,6)
        luck = 12 + dice_sum(1,6)
        return cls(name,skill,stamina,luck)





'''Jim = Character("Jim",1,5)
Tim = Character("Tim",5,1)
Him = Character("Him",50,50)
Kim = Character("Kim",5,5)


Bim = PlayerCharacter.generate_player_character("Bim")

print(Bim.__repr__())'''