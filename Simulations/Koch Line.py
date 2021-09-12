import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption("Koch Line")
screen = pygame.display.set_mode((width, height))

angle = math.pi / 3

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), [self.start[0], self.start[1]], [self.end[0], self.end[1]], 1)

lines = [Line([width / 2, 0],              [width - 100, height - 200]),
         Line([width - 100, height - 200], [100, height - 200]),
         Line([100, height - 200],         [width / 2, 0])]

def generate():
    global lines, angle
    newLines = []
    for line in lines:
        a = line.start
        e = line.end
        b = [line.start[0] + (line.end[0] - line.start[0]) / 3, line.start[1] + (line.end[1] - line.start[1]) / 3]
        d = [line.end[0] - (line.end[0] - line.start[0]) / 3, line.end[1] - (line.end[1] - line.start[1]) / 3]
        c = [math.cos(angle) * (b[0] - d[0]) - math.sin(angle) * (b[1] - d[1]) + d[0], math.sin(angle) * (b[0] - d[0]) + math.cos(angle) * (b[1] - d[1]) + d[1]]

        newLines.append(Line(a, b))
        newLines.append(Line(b, c))
        newLines.append(Line(c, d))
        newLines.append(Line(d, e))

    lines = newLines


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                generate()

def draw():
    screen.fill((255, 255, 255))

    for line in lines:
        line.draw()

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
