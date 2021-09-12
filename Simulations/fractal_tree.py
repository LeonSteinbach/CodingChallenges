import sys
import pygame
import random
from math import sin, cos, pi
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption('Fractal Tree')
screen = pygame.display.set_mode((width, height))

delta = pi / 4


def map(value, x1, y1, x2, y2):
    return (value - x1) * (y2 - x2) / (y1 - x1) + x2


def draw_line(x, y, length, angle):
    if length <= 1:
        return False
    else:
        x2, y2 = length * cos(angle) + x, length * sin(angle) + y
        pygame.draw.line(screen, (255, 255, 255), [x, y], [x2, y2])
        draw_line(x2, y2, length * delta_length, angle + delta_angle)
        draw_line(x2, y2, length * delta_length, angle - delta_angle)


def update():
    global delta_angle, delta_length
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pos = pygame.mouse.get_pos()
    delta_angle = map(pos[0], 0, width, 0, pi)
    delta_length = map(pos[1], 0, height, 0, 0.7)


def draw():
    screen.fill((0, 0, 0))

    draw_line(width / 2, height, height / 2, -pi / 2)


def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)


main()
