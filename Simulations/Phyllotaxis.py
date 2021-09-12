import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 500, 500
pygame.display.set_caption("")
screen = pygame.display.set_mode((width, height))

n = 0
c = 10
deg = 1.6180339887

def update():
    global n, c, deg
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

    screen.fill((0, 0, 0))

    for n in range(100):
        a = n * deg
        r = c * math.sqrt(n)
        x = r * math.cos(a) + width / 2
        y = r * math.sin(a) + height / 2

        pygame.draw.ellipse(screen, (255, 255, 255), [x, y, 10, 10], 1)
    deg += 0.0001

def main():
    while True:
        update()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
