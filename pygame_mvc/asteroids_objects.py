import pygame
import random
import math
from pygame.math import Vector2
from pygame.transform import rotozoom
pygame.init()

class Game:
    def __init__(self,width,height):
        self.twidth = width
        self.theight = height
        self.screen = Screen(800,600,width,height)
        self.contents = []
        self.running = True
        self.player = Player(width/2,height/2)

    def add_asteroids(self):
        self.contents.append(Asteroid(random.randint(0,self.twidth),random.randint(0,self.theight),random.randint(10,20)))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                pygame.quit()


    def process_game_logic(self):
        if len(self.contents) < 10:
            self.add_asteroids()

    def draw(self):
        self.screen.display(self.contents+[self.player])

    def mainloop(self):
        while self.running:

            self.process_game_logic()
            self.draw()
            self.handle_input()

class Asteroid:
    def __init__(self,x,y,radius,resolution = 10):
        self.rad = radius
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.vertices = []
        self.create_vertices(resolution)

    def create_vertices(self,res):
        for i in range(res):
            angle = 2*math.pi * i/res
            x = math.cos(angle)*(self.rad-random.randint(-2,self.rad//4*1))
            y = math.sin(angle)*(self.rad+random.randint(-2,self.rad//4*1))
            self.vertices.append((x,y))

    def relate(self,coords):
            x = coords[0]
            y = coords[1]
            return(x+self.x,y+self.y)

    def convert_coords(self,coords,xmultiplier,ymultiplier):
        (x,y) = coords
        x*=xmultiplier
        y*=ymultiplier
        return(x,y)

    def draw(self,myframe):


        for i in range(len(self.vertices)):
            pygame.draw.line(myframe.frame,('white'),self.convert_coords(self.relate(self.vertices[i]),myframe.xmultiplier,myframe.ymultiplier),self.convert_coords(self.relate(self.vertices[i-1]),myframe.xmultiplier,myframe.ymultiplier),1)


class Screen:
    def __init__(self,width,height,twidth,theight):
        self.truewidth = twidth
        self.trueheight = theight
        self.w = width
        self.h = height
        self.xmultiplier = self.truewidth/self.w
        self.ymultiplier = self.trueheight/self.h
        self.frame = pygame.display.set_mode((self.w, self.h))


    def display(self,things):
        self.frame.fill((0,0,0))
        for thing in things:
            thing.draw(self)
        pygame.display.flip()

class Player:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = Vector2(0,-1)
        self.av = 0
        self.vx = 0
        self.vy = 0

    def accelerate(self,thrust):
        self.vx += thrust*math.cos(math.radians(self.angle))
        self.vy += thrust*math.sin(math.radians(self.angle))

    def angularacc(self,thrust):
        self.av += thrust


    def draw(self, surface):
        UP = Vector2(0, -1)
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

