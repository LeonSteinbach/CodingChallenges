import os
import sys
import pygame
import numpy
from math import sin, cos, pi, sqrt
from random import random, randint, choice
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption('Game of Life')
screen = pygame.display.set_mode((width, height))

running = False

neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def create_array():
    global array, next, array_size, tile_size
    array_size = 100
    tile_size = width // array_size
    array = numpy.zeros((array_size, array_size))
    next = numpy.zeros((array_size, array_size))

    for y in range(array_size):
        for x in range(array_size):
            if randint(0, 100) < 50:
                array[x, y] = 1


def update():
    global array, next, running
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False if running else True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = pygame.mouse.get_pos()[0] // tile_size
                y = pygame.mouse.get_pos()[1] // tile_size
                array[x, y] = 1 if array[x, y] == 0 else 0
                next[x, y] = array[x, y]

    if running:
        for y in range(array_size):
            for x in range(array_size):
                count_n = 0
                for n in neighbors:
                    if 0 <= x+n[0] < array_size-1 and 0 <= y+n[1] < array_size-1:
                        if array[x+n[0], y+n[1]] == 1:
                            count_n += 1

                if count_n > 3 or count_n < 2:
                    next[x, y] = 0
                elif count_n == 3:
                    next[x, y] = 1


def draw():
    screen.fill((255, 255, 255))

    for y in range(array_size):
        for x in range(array_size):
            if running:
                array[x, y] = next[x, y]
            if array[x, y] == 1:
                pygame.draw.rect(screen, (0, 0, 0), [x * tile_size, y * tile_size, tile_size, tile_size])


def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    create_array()
    main()
