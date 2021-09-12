import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1500, 1000
pygame.display.set_caption("")
screen = pygame.display.set_mode((width, height))

screen.fill((255, 255, 255))

points = [[int(width / 2), 50], [50, height - 50], [width - 50, height - 50]]
for point in points:
    pygame.draw.circle(screen, (0, 0, 0), point, 10)

i = random.randint(0, 2)
pos = [points[i][0], points[i][1]]

run = False

def update():
    global pos
    index = random.randint(0, 2)
    pos[0] += (points[index][0] - pos[0]) / 2
    pos[1] += (points[index][1] - pos[1]) / 2

    pygame.draw.rect(screen, (int(pos[1] / 4), 0, int(pos[0] / 6)), [pos[0], pos[1], 3, 3])

def main():
    global run
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    run = True

        if run:
            update()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
