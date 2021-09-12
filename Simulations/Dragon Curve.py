import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1000, 1000
pygame.display.set_caption("Dragon Curve")
screen = pygame.display.set_mode((width, height))

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), self.start, self.end, 1)

lines = []
lines.append(Line([width * 0.3, height / 2], [width * 0.8, height / 2]))

def generate():
    global lines
    newLines = []
    for i in range(len(lines)):
        if i % 2 == 0:
            k = -1
        else:
            k = 1

        a = lines[i].start
        c = lines[i].end

        ac = [c[0] - a[0], c[1] - a[1]]
        aclength = math.sqrt((ac[0] * ac[0]) + (ac[1] * ac[1]))
        acnorm = [ac[0] / aclength, ac[1] / aclength]
        m = [a[0] + acnorm[0] * aclength / 2, a[1] + acnorm[1] * aclength / 2]
        mbrv = [-acnorm[1], acnorm[0]]
        h = aclength / 2
        b = [m[0] + mbrv[0] * h * k, m[1] + mbrv[1] * h * k]

        newLines.append(Line(a, b))
        newLines.append(Line(b, c))

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
