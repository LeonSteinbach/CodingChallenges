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
pygame.display.set_caption('A Star')
screen = pygame.display.set_mode((width, height))

running = False


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.f = 0
        self.g = 0
        self.h = 0

        self.wall = True if randint(0, 100) < 20 else False

        self.parent = None
        self.neighbors = []

    def show(self, color):
        if self.wall:
            color = (0, 0, 0)
        pygame.draw.rect(screen, color, [self.x * tile_size[0],
                                                   self.y * tile_size[1],
                                                   tile_size[0] - 1,
                                                   tile_size[1] - 1])


def create_array():
    global size, grid, OPEN, CLOSED, start, end, tile_size, path, done
    done = False
    
    size = [50, 50]
    tile_size = [width // size[0], height // size[1]]

    grid = []
    for y in range(size[1]):
        row = []
        for x in range(size[0]):
            row.append(Node(x, y))
        grid.append(row)

    start = grid[0][0]
    end = grid[size[1]-1][size[0]-1]

    OPEN = [start]
    CLOSED = []

    path = []

    calculate_neighbors()


def calculate_neighbors():
    for y in range(size[1]):
        for x in range(size[0]):
            if x < size[0] - 1: grid[y][x].neighbors.append(grid[y][x + 1])
            if x > 0:           grid[y][x].neighbors.append(grid[y][x - 1])
            if y < size[1] - 1: grid[y][x].neighbors.append(grid[y + 1][x])
            if y > 0:           grid[y][x].neighbors.append(grid[y - 1][x])
            if x > 0 and y > 0 and grid[y][x-1].wall == False and grid[y-1][x].wall == False:                     grid[y][x].neighbors.append(grid[y - 1][x - 1])
            if x < size[0] - 1 and y > 0 and grid[y][x+1].wall == False and grid[y-1][x].wall == False:           grid[y][x].neighbors.append(grid[y - 1][x + 1])
            if x > 0 and y < size[1] - 1 and grid[y][x-1].wall == False and grid[y+1][x].wall == False:           grid[y][x].neighbors.append(grid[y + 1][x - 1])
            if x < size[0] - 1 and y < size[1] - 1 and grid[y][x+1].wall == False and grid[y+1][x].wall == False: grid[y][x].neighbors.append(grid[y + 1][x + 1])

            grid[y][x].h = heuristic(grid[y][x], end)


def heuristic(a, b):
    return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


def reconstruct():
    global current, path
    path = []
    path.append(current)
    while current.parent:
        path.append(current.parent)
        current = current.parent


def update():
    global running, OPEN, CLOSED, path
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                create_array()
                for y in range(size[1]):
                    for x in range(size[0]):
                        grid[y][x].wall = False
                calculate_neighbors()
                running = False
            if event.key == pygame.K_s:
                create_array()
                running = False
            if event.key == pygame.K_SPACE:
                running = False if running else True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                OPEN = [start]
                CLOSED = []
                path = []
                grid[pos[1] // tile_size[1]][pos[0] // tile_size[0]].wall = True
            if event.button == 3:
                grid[pos[1] // tile_size[1]][pos[0] // tile_size[0]].wall = False
                OPEN = [start]
                CLOSED = []
                path = []


def draw():
    global grid, path, done, current
    screen.fill((0, 0, 0))

    if running:
        if len(OPEN) > 0 and not done:
            current = sorted(OPEN, key=lambda x: x.f)[0]

            if current == end:
                done = True
                reconstruct()
                return

            OPEN.remove(current)
            CLOSED.append(current)

            for neighbor in current.neighbors:
                if neighbor in CLOSED or neighbor.wall:
                    continue

                temp_g = current.g + 1
                if neighbor in OPEN:
                    if temp_g < neighbor.g:
                        neighbor.g = temp_g
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.parent = current
                else:
                    neighbor.g = temp_g
                    OPEN.append(neighbor)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current
                

        elif len(OPEN) == 0 and not done:
            print('No Solution')
            done = True

        if not done:
            reconstruct()

    for y in range(size[1]):
        for x in range(size[0]):
            if grid[y][x] in path:
                grid[y][x].show((150, 150, 255))
            elif grid[y][x] in OPEN:
                grid[y][x].show((0, 255, 0))
            elif grid[y][x] in CLOSED:
                grid[y][x].show((255, 0, 0))
            else:
                grid[y][x].show((255, 255, 255))


def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    create_array()
    main()
