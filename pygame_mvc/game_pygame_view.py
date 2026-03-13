import pygame
from game_objects import *

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class display_object:
    def __init__(self,file,width,height):
        pygame.init()
        self.width = width
        self.height = height
        self.sprite = pygame.image.load(file).convert_alpha()






class screen:
    key_moves = {K_UP: 'w1',
                 K_DOWN: 's1',
                 K_RIGHT: 'd1',
                 K_LEFT: 'a1',
                 K_w:'w0',
                 K_s:'s0',
                 K_d:'d0',
                 K_a:'a0'
                 }
    def __init__(self,screenwidth,screenheight,background):
        pygame.init()
        pygame.display.set_caption('Pygame MVC')
        self.game = Game()
        self.game.set_background_from_file(background)
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.frame = pygame.display.set_mode((screenwidth,screenheight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.numplayers = 0
        self.colourpalette = {'S':'cyan','W':'red','F':'gray','E':'red','C':'pink','T':'blue'}

    def _handle_input(self):
        """ Checks key presses and adjusts GameGUI attributes depending on the presses """

        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            #Checks for movement
            for item in self.key_moves.keys():

                if (event.type == KEYDOWN and event.key == item):
                    #print(self.key_moves[item])
                    if self.numplayers == 2:
                        self.game.characters[int(self.key_moves[item][1])].try_to_move(self.key_moves[item][0].upper())
                    else:
                        self.game.characters[0].try_to_move(self.key_moves[item][0].upper())
            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None

    def draw_a_rect(self,thing):
        colour = self.colourpalette[thing.kind]

        visualpos = self.convertpos(thing.pos)
        displayrect = pygame.Rect(*visualpos, *self.cell_dimensions())
        pygame.draw.rect(self.frame,colour,displayrect)
        if thing.kind == 'W':
            aestheticcolour = 'tan'
            (ax,ay) = visualpos
            ax+=1
            ay+=1
            (aw,ah) = self.cell_dimensions()
            aw-=2
            ah-=2
            arect = pygame.Rect(ax,ay,aw,ah)
            pygame.draw.rect(self.frame,aestheticcolour,arect)


    def draw_a_circle(self,thing):
        if thing.kind == 'C':
            colour = self.colourpalette[thing.name[0]]
        else:
            colour = self.colourpalette[thing.kind]
        visualpos = self.convertpos(thing.pos)
        (x,y) = visualpos
        x+=self.cell_dimensions()[0]/2
        y+=self.cell_dimensions()[1]/2
        pygame.draw.circle(self.frame,colour,(x,y),min(self.cell_dimensions())//2)

    def draw_sprite(self,thing):
        sprite = thing.displayer


    def convertpos(self,pos):
        (x,y) = pos
        visualx = x/self.game.dimensions[0]*self.screenwidth
        visualy = y/self.game.dimensions[1]*self.screenheight
        return (visualx,visualy)

    def cell_dimensions(self):
        x = self.screenwidth/self.game.dimensions[0]
        y = self.screenheight/self.game.dimensions[1]
        return (int(x),int(y))

    def set_up_characters(self,numplayers):
        self.numplayers = numplayers
        names = ['Carl','Tilly','John','Petra']
        for i in range(self.numplayers):
            self.game.add_mc(names[i])


    def draweverything(self):
        self.frame.fill((0,0,0))
        for thing in self.game.backgrounds:
            self.draw_a_rect(thing)
        for character in self.game.characters:
            self.draw_a_circle(character)
        pygame.display.flip()

    def game_loop(self):
        while self.running:
            self._handle_input()
            self.draweverything()
            self.clock.tick(60)

thescreen = screen(800,800,'background.txt')

thescreen.set_up_characters(2)

thescreen.game_loop()
