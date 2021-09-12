import sys
import pygame
import random
from math import sin, cos, pi, sqrt
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption('Cardioid')
screen = pygame.display.set_mode((width, height))

running = False

radius = 350
n = 80
c = 0


def create_points():
    global points
    points = []
    m = (width // 2, height // 2)
    for i in range(n):
        angle = i * (360.0 / n) * pi / 180
        x = radius * cos(angle) + m[0]
        y = radius * sin(angle) + m[1]
        points.append([x, y]);


def draw():
    global c, running
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                running = True

    if running:
        create_points()
        c += 0.1

        screen.fill((0, 0, 0))
        for point in points:
            pygame.draw.circle(screen, (255, 255, 255), [int(point[0]), int(point[1])], 2)

        for i in range(n):
            p = points[int((i * (n-1) + c)) % n]
            pygame.draw.line(screen, (255, 255, 255), points[i], p)


def main():
    while True:
        draw()
        pygame.display.flip()
        fpsClock.tick(fps)


main()
