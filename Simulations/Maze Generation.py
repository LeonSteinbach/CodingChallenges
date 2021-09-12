import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption("Maze Generation")
screen = pygame.display.set_mode((width, height))

fieldSize = 20
arraySize = [int(math.floor(width / fieldSize)), int(math.floor(height / fieldSize))]

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]

    def draw(self):
        if (self.walls[0]):
            pygame.draw.line(screen, (0, 0, 0), [self.x * fieldSize, self.y * fieldSize], [self.x * fieldSize + fieldSize, self.y * fieldSize], 2)
        if (self.walls[1]):
            pygame.draw.line(screen, (0, 0, 0), [self.x * fieldSize + fieldSize, self.y * fieldSize], [self.x * fieldSize + fieldSize, self.y * fieldSize + fieldSize], 2)
        if (self.walls[2]):
            pygame.draw.line(screen, (0, 0, 0), [self.x * fieldSize + fieldSize, self.y * fieldSize + fieldSize], [self.x * fieldSize, self.y * fieldSize + fieldSize], 2)
        if (self.walls[3]):
            pygame.draw.line(screen, (0, 0, 0), [self.x * fieldSize, self.y * fieldSize + fieldSize], [self.x * fieldSize, self.y * fieldSize], 2)

cells = []
visited = []
stack = []

for y in range(arraySize[0]):
    for x in range(arraySize[1]):
        cells.append(Cell(x, y))

current = cells[0]
visited.append(current)

def index(x, y):
    return x + y * arraySize[0]

def update():
    global current
    if len(visited) < len(cells):
        neighbors = []
        if current.y > 0:
            if cells[index(current.x, current.y - 1)] not in visited:
                neighbors.append(cells[index(current.x, current.y - 1)])
        if current.x < arraySize[0] - 1:
            if cells[index(current.x + 1, current.y)] not in visited:
                neighbors.append(cells[index(current.x + 1, current.y)])
        if current.y < arraySize[1] - 1:
            if cells[index(current.x, current.y + 1)] not in visited:
                neighbors.append(cells[index(current.x, current.y + 1)])
        if current.x > 0:
            if cells[index(current.x - 1, current.y)] not in visited:
                neighbors.append(cells[index(current.x - 1, current.y)])

        if (len(neighbors) > 0):
            choosen = neighbors[random.randint(0, len(neighbors) - 1)]

            if (current.x > choosen.x):
                current.walls[3] = False
                choosen.walls[1] = False
            if (current.x < choosen.x):
                current.walls[1] = False
                choosen.walls[3] = False
            if (current.y > choosen.y):
                current.walls[0] = False
                choosen.walls[2] = False
            if (current.y < choosen.y):
                current.walls[2] = False
                choosen.walls[0] = False

            current = choosen

            visited.append(current)
            stack.append(current)

        else:
            if len(stack) > 0:
                current = stack[-1]
                stack.pop()

def draw():
    for cell in cells:
        cell.draw()

    if len(visited) < len(cells):
        pygame.draw.rect(screen, (0, 0, 0), [current.x * fieldSize, current.y * fieldSize, fieldSize, fieldSize])

def main():
    while True:
      screen.fill((255, 255, 255))

      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

      update()
      draw()

      pygame.display.flip()
      fpsClock.tick(fps)

main()
