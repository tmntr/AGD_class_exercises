import pygame
from game_objects import *

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class screen:
    key_moves = {K_UP: 'n',
                 K_DOWN: 's',
                 K_RIGHT: 'e',
                 K_LEFT: 'w',
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
        self.colourpalette = {'S':'cyan','W':'orange','F':'black','E':'red','C':'pink'}

    def _handle_input(self):
        """ Checks key presses and adjusts GameGUI attributes depending on the presses """

        for event in pygame.event.get():
            # Quit conditions
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False

            # Checks for movement keys amd sets self.move_direction according to the key pressed.
            # Otherwise, set self.move_direction to None

    def draw_a_thing(self,thing):
        colour = self.colourpalette[thing.kind]
        visualpos = self.convertpos(thing.pos)
        displayrect = pygame.Rect(*self.convertpos(thing.pos), *self.cell_dimensions())
        pygame.draw.rect(self.frame,colour,displayrect)

    def convertpos(self,pos):
        (x,y) = pos
        visualx = x/self.game.dimensions[0]*self.screenwidth
        visualy = y/self.game.dimensions[1]*self.screenheight
        return (visualx,visualy)

    def cell_dimensions(self):
        x = self.screenwidth/self.game.dimensions[0]
        y = self.screenheight/self.game.dimensions[1]
        return (int(x),int(y))

    def set_up_characters(self):
        self.game.add_mc('Carl')

    def draweverything(self):
        self.frame.fill((0,0,0))
        for thing in self.game.backgrounds:
            self.draw_a_thing(thing)
        for character in self.game.characters:
            self.draw_a_thing(character)
        pygame.display.flip()

    def game_loop(self):
        while self.running:
            self.draweverything()
            self.clock.tick(60)

thescreen = screen(800,600,'background.txt')

thescreen.set_up_characters()

thescreen.game_loop()
