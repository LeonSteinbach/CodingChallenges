import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1400, 1000
pygame.display.set_caption("Circle Recursion")
screen = pygame.display.set_mode((width, height))

run = False

screen.fill((255, 255, 255))

def drawCircle(x, y, d):
    pygame.draw.ellipse(screen, (0, 0, 0), [x - d / 2, y - d / 2, d, d], 1)

    if d > 3:
        drawCircle(x + d / 2, y, d / 2)
        drawCircle(x - d / 2, y, d / 2)
        drawCircle(x, y + d / 2, d / 2)
    pygame.display.flip()

def main():
    global run
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if run == False:
                        run = True
                        drawCircle(width / 2, height / 3, 650)

        pygame.display.flip()
        fpsClock.tick(fps)
main()
