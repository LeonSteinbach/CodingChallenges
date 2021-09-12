import sys
import pygame
from math import *
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1500, 700
pygame.display.set_caption("Function Plot")
screen = pygame.display.set_mode((width, height))

bounds = [-int(width/2), int(width/2), -10, 10]
res = 0.1
origin = [int(width / 2), int(height / 2)]

f = lambda x: x
excluding = []

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def plot():
    global bounds, res, origin, excluding
    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (50, 50, 50), [0, origin[1]], [width, origin[1]], 1)
    pygame.draw.line(screen, (50, 50, 50), [origin[0], 0], [origin[0], height], 1)

    for i in range(origin[0], width, 100):
        pygame.draw.line(screen, (50, 50, 50), [i, origin[1] - 5], [i, origin[1] + 5], 1)
    for i in range(origin[0], 0, -100):
        pygame.draw.line(screen, (50, 50, 50), [i, origin[1] - 5], [i, origin[1] + 5], 1)

    for j in range(origin[1], height, 100):
        pygame.draw.line(screen, (50, 50, 50), [origin[0] - 5, j], [origin[0] + 5, j], 1)
    for j in range(origin[1], 0, -100):
        pygame.draw.line(screen, (50, 50, 50), [origin[0] - 5, j], [origin[0] + 5, j], 1)

    x = bounds[0]
    while x < bounds[1]:
        if -1000000 < -f(x) < 1000000:
            if not round(x-res) in excluding and not round(x) in excluding:
                #print x, -f(x)
                pygame.draw.line(screen, (255, 255, 255), [int(round(x - res)) + origin[0], int(-f(round(x - res))) + origin[1]], [int(round(x)) + origin[0], int(-f(round(x))) + origin[1]], 1)
        x += res

plot()

def main():
    while True:
        update()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
