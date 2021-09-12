import sys
import numpy
import pygame
from pygame.locals import *
from random import randint
from math import floor, sqrt

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

size = 20
nColors = 6

if nColors > 2:
    maxMoves = int((sqrt(nColors - 1) * size / 2 - nColors / 2) * 1.5)
else:
    maxMoves = int(sqrt(nColors - 1) * size / 2 - nColors / 2)

width, height = 500, 600
tileSize = int(floor(min(width, height) / size))

width -= width - size * tileSize

pygame.display.set_caption("Flood it")
screen = pygame.display.set_mode((width, height))

Arial = pygame.font.SysFont('Arial', 30)

array = numpy.zeros((size, size))

neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
flooded = []

def createArray():
    global nColors, moves, loose
    moves = 0
    loose = False
    for y in range(size):
        for x in range(size):
            if nColors >= len(colors):
                nColors = len(colors) - 1
            array[x, y] = randint(0, nColors - 1)

def flood(color, pos):
    flooded.append(pos)
    for neighbor in neighbors:
        if 0 <= pos[0] + neighbor[0] < size and 0 <= pos[1] + neighbor[1] < size:
            if [pos[0] + neighbor[0], pos[1] + neighbor[1]] not in flooded:
                if array[pos[0], pos[1]] == array[pos[0] + neighbor[0], pos[1] + neighbor[1]]:
                    flood(color, [pos[0] + neighbor[0], pos[1] + neighbor[1]])
    array[pos[0], pos[1]] = color

def checkWin():
    for y in range(size):
        for x in range(size):
            if array[x, y] != array[0, 0]:
                return False
    return True

def update():
    global flooded, moves, loose
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not loose:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    flooded = []
                    if array[int(pos[0] / tileSize), int(pos[1] / tileSize)] != array[0, 0]:
                        flood(array[int(pos[0] / tileSize), int(pos[1] / tileSize)], [0, 0])
                        moves += 1

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                createArray()

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if moves >= maxMoves:
        loose = True
    else:
        loose = False

def draw():
    global loose
    screen.fill((255, 255, 255))

    for y in range(size):
        for x in range(size):
            pygame.draw.rect(screen, colors[int(array[x, y])], [x * tileSize, y * tileSize, tileSize, tileSize])

    pygame.draw.rect(screen, (0, 0, 0), [0, height - (height - width), width, 7])
    screen.blit(Arial.render(str(moves) + ' / ' + str(maxMoves), False, (0, 0, 0)), (width / 2 - 20, height - ((height - width) / 2 + 20)))

    if checkWin():
        loose = False
        screen.blit(Arial.render('You Win!', False, (0, 0, 0)), (width / 2 - 40, height - ((height - width) / 2 - 10)))

    if loose:
        screen.blit(Arial.render('You Lost!', False, (0, 0, 0)), (width / 2 - 45, height - ((height - width) / 2 - 10)))

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

if __name__ == '__main__':
    createArray()
    main()
