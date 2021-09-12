import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption('Circle Recursion')
screen = pygame.display.set_mode((width, height))


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

def draw_circle(x, y, radius):
    if radius <= 10:
        return
    else:
        pygame.draw.ellipse(screen, (255, 255, 255), [x - radius / 2, y - radius / 2, radius, radius], 1)
        draw_circle(x + radius / 2, y, radius / 2)
        draw_circle(x - radius / 2, y, radius / 2)
        draw_circle(x, y + radius / 2, radius / 2)
        draw_circle(x, y - radius / 2, radius / 2)

def draw():
    screen.fill((0, 0, 0))

    draw_circle(width / 2, height / 2, width / 2)

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
