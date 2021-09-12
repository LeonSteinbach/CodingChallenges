import sys
import pygame
import math
import random
import numpy
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption("")
screen = pygame.display.set_mode((width, height))

fieldSize = 2
arraySize = int(math.floor(width / fieldSize))
array = numpy.zeros([arraySize, arraySize])

i = 0

x = int(width / 2 / fieldSize)
y = int(height / 2 / fieldSize)
dir = 0
array[x, y] = 1

def update():
    global dir, x, y
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if array[x, y] == 0:
        if dir < 3:
            dir += 1
        else:
            dir = 0
        array[x, y] = 1
        pygame.draw.rect(screen, (0, 0, 0), [x * fieldSize, y * fieldSize, fieldSize, fieldSize])
    elif array[x, y] == 1:
        if dir > 0:
            dir -= 1
        else:
            dir = 3
        array[x, y] = 0
        pygame.draw.rect(screen, (255, 255, 255), [x * fieldSize, y * fieldSize, fieldSize, fieldSize])

    if dir == 0: y -= 1
    elif dir == 1: x += 1
    elif dir == 2: y += 1
    elif dir == 3: x -= 1

    if x < 0: x = arraySize - 1
    if y < 0: y = arraySize - 1
    if x > arraySize - 1: x = 0
    if y > arraySize - 1: y = 0

def main():
    while True:
        update()

        pygame.display.flip()
        fpsClock.tick(fps)

screen.fill((255, 255, 255))
main()
