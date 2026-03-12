class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = (0,0)
        self._start = (0,0)
        self._exit = (0,0)

    @property
    def start(self):
        return self._start

    @property
    def exit(self):
        return self._exit

    def set_up(self,mcname):
        mcname = input("Please enter your name: ")
        self.add_mc(mcname)


    def get_pos_background(self,pos):
        for tile in self.backgrounds:
            if tile.pos == pos:
                return tile

    def anything_there(self,pos):
        return self.get_pos_background(pos).is_solid()

    def not_void(self,pos):
        valid = True
        if pos[0] >= self.dimensions[0] or pos[0] < 0:
            valid = False
        elif pos[1] >= self.dimensions[1] or pos[1] < 0:
            valid = False
        return valid

    def add_background_object(self, thetype: str, thepos: tuple):
        self.backgrounds.append(GameObj(thetype,thepos,self))

    def add_mc(self,name):
        self.characters.append(Character(name,self.find_start(),self))

    def check_for_win(self):
        winners = []
        for mchar in self.characters:
            if mchar.made_it():
                winners.append(mchar)
        return winners



    def find_start(self):
        thepos = (0,0)
        for b in self.backgrounds:
            if b.kind == 'S':
                thepos = b.pos
        return thepos

    def find_ends(self):
        theposs = []
        for b in self.backgrounds:
            if b.kind == 'E':
                theposs.append(b.pos)
        return theposs


    def set_background_from_file(self,filename):
        with open(filename,'r') as filey:
            y = 0
            for line in filey.readlines():
                line = line.strip()
                x = 0
                for letter in line.split(','):
                    self.backgrounds.append(Tile(letter,(x,y),self))
                    x+=1
                y += 1
            self.dimensions = (x,y)

            print(self.dimensions)
    def textdisplay(self):
        print('╔'+'═'*self.dimensions[0]+'╗')
        thegrid = [['' for i in range(self.dimensions[0])] for j in range(self.dimensions[1])]
        for b in self.backgrounds:
            thegrid[b.y][b.x] = b.textrepresent()
        for char in self.characters:
            thegrid[char.y][char.x] = char.name[0]
        for line in thegrid:
            print('║'+''.join(line)+'║')
        print('╚' + '═' * self.dimensions[0] + '╝')


class GameObj:
    def __init__(self,kind,pos,game):
        self.kind = kind
        self.pos = pos
        self.game = game

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]


    def textrepresent(self):
        if self.kind == 'S':
            return '\u2591'
        elif self.kind == 'W':
            return '\u2588'
        elif self.kind == 'E':
            return '\u2593'
        elif self.kind == 'F':
            return ' '
        else:
            return '?'
    def __str__(self) -> str:
        pass

    def is_solid(self):
        return self.kind == 'W'



class Character(GameObj):
    def __init__(self,name,pos,game):
        super().__init__('C',pos,game)
        self.name = name

    def find_next_location(self,direction: str):
        (x,y) = self.pos
        if direction == 'W':
            y  -= 1
        elif direction == 'S':
            y += 1
        elif direction == 'A':
            x -= 1
        elif direction == 'D':
            x += 1
        return (x,y)

    def moveable(self,direction: str):
        proposed_pos = self.find_next_location(direction)
        if self.game.not_void(proposed_pos):
            if self.game.anything_there(proposed_pos):
                return False
            else:
                return True
        else:
            return False

    def move(self,direction: str):
        self.pos = self.find_next_location(direction)

    def try_to_move(self,direction: str):
        if self.moveable(direction):
            self.move(direction)

    def made_it(self):
        if self.pos in self.game.find_ends():
            return True
        else:
            return False



class Tile(GameObj):
    def __init__(self,kind,pos,game,contents = []):
        super().__init__(kind,pos,game)
        self.contents = contents

    def __str__(self):
        return f'{self.kind}'

'''thegame = Game()

thegame.set_background_from_file('background.txt')

thegame.set_up()

while True:
    for char in thegame.characters:
        thegame.display()
        direction = input("Please enter your direction (WASD): ")
        char.try_to_move(direction)'''