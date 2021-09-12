import sys
import pygame
from math import pi, sin, cos
from pygame.locals import *

pygame.init()
fps = 1000
fpsClock = pygame.time.Clock()
width, height = 800, 800
pygame.display.set_caption('Heart Curve')
screen = pygame.display.set_mode((width, height))
res = 0
t = 0

def draw():
    global res, t
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    t += 0.001
    res = (sin(t) + 1.01)

    points = []
    angle = 0
    while angle < pi * 2:
        r = 10
        x = r * 16 * sin(angle) ** 3 + width // 2
        y = r * -(13 * cos(angle) - 5 * cos(2 * angle) - 2 * cos(3 * angle) - cos(4 * angle)) + height // 2
        points.append([x, y])
        angle += res

    pygame.draw.lines(screen, (255, 255, 255), True, points)

def main():
    while True:
        draw()
        pygame.display.flip()
        fpsClock.tick(fps)

main()
