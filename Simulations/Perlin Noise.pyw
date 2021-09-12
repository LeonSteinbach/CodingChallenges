import sys
import pygame
import math
import random
from Vec2 import *
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1500, 1000
pygame.display.set_caption("Perlin Noise")
screen = pygame.display.set_mode((width, height))

def createNoise():
    length = 1500
    final = [0 for i in range(length)]
    d = 10
    for i in range(5):
        array = [0]
        for i in range(length):
            if i % d == 0:
                vectorY = (random.randint(1, 100) - 50) / 10.0
            array.append(array[i] + vectorY)

        for c in range(length):
            final[c] += int(array[c])
        if d > 0: d /= 2
        if d <= 0: d = 1

    return final

array = createNoise()
print(array)

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

def draw():
    screen.fill((0, 0, 0))

    for i in range(len(array) - 1):
        pygame.draw.line(screen, (255, 255, 255), [i, array[i] + 500], [i + 1, array[i + 1] + 500], 1)


def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
