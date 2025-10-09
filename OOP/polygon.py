import math

import numpy as np

import matplotlib.pyplot as plt

from math import sqrt



class Coord:

    def __init__(self, x1: float, y1: float):

        self.point = np.array((x1, y1))
        self.x = self.point[0]
        self.y = self.point[1]

    def distance(self, other) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2+dy**2)



class Polygon:

    def __init__(self, points: list[Coord]):

        self.points = points


    def perimeter(self) -> float:

        pass


    def plot(self):

        pass



class Triangle(Polygon):

    def __init__(self, p0: Coord, p1: Coord, p2: Coord):

        pass


    def area(self) -> float:

        pass