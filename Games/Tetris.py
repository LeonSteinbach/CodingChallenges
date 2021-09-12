import sys
import pygame
import math
import random
import numpy
from time import time
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 400, 800
pygame.display.set_caption("Tetris")
screen = pygame.display.set_mode((width, height))

figures = [
    [
        [0,0,0,0],
        [0,0,0,0],
        [1,1,1,1],
        [0,0,0,0]
    ],
    [
        [0,0,0],
        [1,1,1],
        [1,0,0]
    ],
    [
        [0,0,0],
        [1,1,1],
        [0,0,1]
    ],
    [
        [0,0,0],
        [0,1,1],
        [1,1,0]
    ],
    [
        [0,0,0],
        [1,1,0],
        [0,1,1]
    ],
    [
        [0,0,0],
        [1,1,1],
        [0,1,0]
    ],
    [
        [1,1],
        [1,1]
    ]
]

size = [10, 20]
tileSize = width / size[0]

array = numpy.zeros(size)

current = figures[random.randint(0, len(figures) - 1)].copy()
cx = int(size[0] / 2) - math.floor(len(current) / 2)
cy = 0

rotation = 0

timer = time()

down = False

baseSpeed = 0.4
speed = baseSpeed
maxSpeed = 0.05
downSpeed = 0.05
speedChange = 0.0001

def rotate(matrix, n):
    length = len(matrix)
    for z in range(n):
        for row in range(int(length / 2)):
            for col in range(row, length - 1 - row):
                tmpVal = matrix[row][col]
                for i in range(4):
                    rowSwap = col
                    colSwap = (length - 1) - row
                    poppedVal = matrix[rowSwap][colSwap]
                    matrix[rowSwap][colSwap] = tmpVal
                    tmpVal = poppedVal
                    col = colSwap
                    row = rowSwap

def spawn():
    global current, cx, cy, rotation
    current = figures[random.randint(0, len(figures) - 1)].copy()
    cx = int(size[0] / 2) - math.floor(len(current) / 2)
    cy = 0

    rotate(current, 4-rotation)
    rotation = 0

def collide():
    for y in range(len(current)):
        for x in range(len(current)):
            if current[x][y] == 1:
                array[x+cx][y+cy] = current[x][y]

def canMove(dx):
    for y in range(len(current)):
        for x in range(len(current)):
            if current[x][y] == 1 and (cx+x+dx < 0 or cx+x+dx > size[0]-1 or array[cx+x+dx][cy+y] == 1):
                return False
    return True

def checkRows():
    global array
    counter = 0
    for y in range(size[1]):
        delete = True
        for x in range(size[0]):
            if array[x][y] == 0:
                delete = False
        if delete:
            for x in range(size[0]):
                array[x][y] = 0
            counter += 1
            for j in range(y, 0, -1):
                for i in range(size[0]):
                    array[i][j] = array[i][j-1]

def isLost():
    for x in range(size[0]):
        if array[x][0] == 1:
            return True
    return False

def update():
    global timer, cx, cy, current, array, rotation, speed, baseSpeed
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                rotate(current, 3)
                if not canMove(0):
                    rotate(current, 1)
                else:
                    rotation = rotation - 1 if rotation > 0 else 3
            if event.key == pygame.K_z:
                rotate(current, 1)
                if not canMove(0):
                    rotate(current, 3)
                else:
                    rotation = rotation + 1 if rotation < 3 else 0

            if event.key == pygame.K_RIGHT:
                if canMove(1):
                    cx += 1
            if event.key == pygame.K_LEFT:
                if canMove(-1):
                    cx -= 1
            if event.key == pygame.K_DOWN:
                speed = downSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                speed = baseSpeed

    if time() - timer > speed:
        timer = time()
        for y in range(len(current)):
            for x in range(len(current)):
                if current[x][y] == 1:
                    if cy + y >= size[1]-1 or array[x+cx][y+cy+1] == 1:
                        collide()
                        spawn()
                        return
        cy += 1

        if speed > maxSpeed:
            baseSpeed -= speedChange
            speed -= speedChange

    checkRows()
    if isLost():
        array = numpy.zeros(size)
        spawn()

def draw():
    screen.fill((0, 0, 0))

    for y in range(size[1]):
        for x in range(size[0]):
            if array[x][y] == 0:
                pygame.draw.rect(screen, (255, 255, 255), [x * tileSize, y * tileSize, tileSize - 1, tileSize - 1])
            elif array[x][y] == 1:
                pygame.draw.rect(screen, (100, 100, 100), [x * tileSize, y * tileSize, tileSize - 1, tileSize - 1])

    for y in range(len(current)):
        for x in range(len(current[0])):
            if current[x][y] == 1:
                pygame.draw.rect(screen, (0, 0, 255), [(cx + x) * tileSize, (cy + y) * tileSize, tileSize - 1, tileSize - 1])

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
