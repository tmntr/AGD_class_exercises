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

    def set_up(self):
        pass

    def add_background_object(self, thetype: str, thepos: tuple):
        self.backgrounds.append(GameObj(thetype,thepos))

    def set_background_from_file(self,filename):
        with open(filename,'r') as filey:
            y = 0
            for line in filey.readlines():
                line = line.strip()
                x = 0
                for letter in line:
                    self.backgrounds.append(Tile(letter,(x,y)))
                    x+=1
                y += 1
            self.dimensions = (x,y)

            print(self.dimensions)
    def display(self):
        thegrid = [['' for i in range(self.dimensions[0])] for j in range(self.dimensions[1])]
        for b in self.backgrounds:
            thegrid[b.y][b.x] = b.__str__()
        for line in thegrid:
            print(''.join(line))


class GameObj:
    def __init__(self,kind,pos):
        self.kind = kind
        self.pos = pos

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    def __str__(self) -> str:
        pass

    def is_solid(self):
        return self.kind == 'W'



class Character(GameObj):
    def __init__(self,name,kind,pos):
        super().__init__(kind,pos)
        self.name = name

    def find_next_location(self,direction: str):





class Tile(GameObj):
    def __init__(self,kind,pos,contents = []):
        super().__init__(kind,pos)
        self.contents = contents

    def __str__(self):
        return f'{self.kind}'

thegame = Game()

thegame.set_background_from_file('background.txt')

thegame.display()