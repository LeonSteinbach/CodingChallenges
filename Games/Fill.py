import sys
import pygame
import numpy
from random import randint, choice
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption("Fill")
screen = pygame.display.set_mode((width, height))

size = 10
tileSize = int(min(width, height) / size)

bSize = [200, 100]
button = [width / 2 - bSize[0] / 2, height / 2 - bSize[1] / 2, bSize[0], bSize[1]]

Arial = pygame.font.SysFont('Arial', 30)
nextLevelText = Arial.render('Next level', False, (0, 0, 0))

level = 3

def createArray(l):
    global array, start, path, win
    win = False
    start = [randint(1, size - 2), randint(1, size - 2)]
    array = numpy.zeros((size, size))
    current = start
    path = [start]
    array[start[0], start[1]] = 1
    neighbors = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    last = [0, 0]
    for n in range(l):
        possible = []
        for nb in neighbors:
            if 0 <= current[0] + nb[0] < size - 1 and 0 <= current[1] + nb[1] < size - 1 and nb != last and array[current[0] + nb[0], current[1] + nb[1]] == 0:
                possible.append(nb)
        if len(possible) == 0:
            break
        new = choice(possible)
        last = new
        array[current[0] + new[0], current[1] + new[1]] = 1
        current = [current[0] + new[0], current[1] + new[1]]

def checkWin():
    for y in range(size):
        for x in range(size):
            if array[x, y] == 1 and [x, y] not in path:
                return False
    return True

def update():
    global win, level
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if win and button[0] <= pos[0] <= button[0] + button[2] and button[1] <= pos[1] <= button[1] + button[3]:
                    level += 2
                    createArray(level)

    if pygame.mouse.get_pressed() == (1, 0, 0):
        pos = [int(pygame.mouse.get_pos()[0] / tileSize), int(pygame.mouse.get_pos()[1] / tileSize)]

        if abs(pos[0]-path[-1][0]) + abs(pos[1]-path[-1][1]) == 1 and array[pos[0], pos[1]] == 1 and pos not in path:
            path.append(pos)
        if len(path) > 1 and pos == path[-2]:
            del path[-1]

    win = checkWin()

def draw():
    screen.fill((0, 0, 0))

    for y in range(size):
        for x in range(size):
            if win:
                if array[x, y] == 1:
                    pygame.draw.rect(screen, (218, 165, 32), [x * tileSize, y * tileSize, tileSize - 1, tileSize - 1])
            else:
                if [x, y] in path:
                    pygame.draw.rect(screen, (100, 100, 200), [x * tileSize, y * tileSize, tileSize - 1, tileSize - 1])
                elif array[x, y] == 1:
                    pygame.draw.rect(screen, (150, 150, 150), [x * tileSize, y * tileSize, tileSize - 1, tileSize - 1])

    for i in range(len(path)-1):
        pygame.draw.line(screen, (0, 0, 0),
                         [path[i][0] * tileSize + tileSize / 2, path[i][1] * tileSize + tileSize / 2],
                         [path[i+1][0] * tileSize + tileSize / 2, path[i+1][1] * tileSize + tileSize / 2], 5)

    if win:
        pos = pygame.mouse.get_pos()
        if button[0] <= pos[0] <= button[0] + button[2] and button[1] <= pos[1] <= button[1] + button[3]:
            pygame.draw.rect(screen, (200, 200, 200), button)
        else:
            pygame.draw.rect(screen, (255, 255, 255), button)
        screen.blit(nextLevelText, (button[0] + 45, button[1] + 30))

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

if __name__ == '__main__':
    createArray(level)
    main()
