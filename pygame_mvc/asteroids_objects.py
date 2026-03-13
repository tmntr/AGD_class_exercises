import pygame
import random
import math

pygame.init()

class Game:
    def __init__(self,width,height):
        self.twidth = width
        self.theight = height
        self.screen = Screen(800,600)
        self.contents = []
        self.running = True

    def add_asteroids

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                pygame.quit()


    def process_game_logic(self):
        pass

    def draw(self):
        self.screen.display(self.contents)

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

    def draw(self,screen,xmultiplier,ymultiplier):
        for i in range(len(self.vertices)):
            pygame.draw.line(screen,('white'),self.convert_coords(self.relate(self.vertices[i])),self.convert(self.relate(self.vertices[i-1])),1)


class Screen:
    def __init__(self,width,height,twidth,theight):
        self.truewidth = twidth
        self.trueheight = theight
        self.w = width
        self.h = height
        self.frame = pygame.display.set_mode((self.w, self.h))


    def display(self,things):
        self.frame.fill((0,0,0))
        for thing in things:
            thing.draw(self.frame)
        pygame.display.flip()

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = 0
        self.av = 0
        self.vx = 0
        self.vy = 0

    def accelerate(self,thrust):
        self.vx += thrust*math.cos(math.radians(self.angle))
        self.vy += thrust*math.sin(math.radians(self.angle))

    def angularacc(self,thrust):
        self.av += thrust

