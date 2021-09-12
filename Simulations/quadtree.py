import sys
import pygame
import math
from random import random, randint
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption('Quad Tree')
screen = pygame.display.set_mode((width, height))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), [self.x, self.y], 5)


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return str(self.x) + ',' + str(self.y) + ',' + str(self.w) + ',' + str(self.h)

    def contains(self, point):
        return ((self.x - self.w < point.x < self.x + self.w) and
                (self.y - self.h < point.y < self.y + self.h))


class Quadtree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

        self.nw, self.ne, self.sw, self.se = None, None, None, None

    def __str__(self):
        return str(len(self.points)) + ' ' + \
               str(self.boundary) + '\n  ' + \
               str(self.nw) + '\n  ' + \
               str(self.ne) + '\n  ' + \
               str(self.sw) + '\n  ' + \
               str(self.se) + '\n'

    def subdivide(self):
        (x, y, w, h) = (self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h)
        self.nw = Quadtree(Rectangle(x - w/2, y - h/2, w/2, h/2), self.capacity)
        self.ne = Quadtree(Rectangle(x + w/2, y - h/2, w/2, h/2), self.capacity)
        self.sw = Quadtree(Rectangle(x - w/2, y + h/2, w/2, h/2), self.capacity)
        self.se = Quadtree(Rectangle(x + w/2, y + h/2, w/2, h/2), self.capacity)
        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return
        if len(self.points) < self.capacity:
            self.points.append(point)
        else:
            if not self.divided:
                self.subdivide()

            self.nw.insert(point)
            self.ne.insert(point)
            self.sw.insert(point)
            self.se.insert(point)

    def draw(self):
        (x, y, w, h) = (self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h)
        pygame.draw.lines(screen, (255, 255, 255), True , [[x-w, y-h],
                                                           [x+w, y-h],
                                                           [x+w, y+h],
                                                           [x-w, y+h]])
        for point in self.points:
            point.draw()

        if self.divided:
            self.nw.draw()
            self.ne.draw()
            self.sw.draw()
            self.se.draw()

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                qt.insert(Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


def draw():
    screen.fill((0, 0, 0))

    qt.draw()

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    qt = Quadtree(Rectangle(400, 400, 400, 400), 4)
    for i in range(16):
        qt.insert(Point(randint(0, width), randint(0, height)))

    print(qt)
    main()
