import sys
import pygame
import math
import random
from pygame.locals import *
import PIL
from PIL import Image

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption("Snowflake")
screen = pygame.display.set_mode((width, height))

files = 0

class Walker:
    def __init__(self, x, y, moving):
        self.x = x
        self.y = y
        self.moving = moving

        self.radius = 5
        self.randomOff = 15
        self.speed = 5

    def collide(self):
        for walker in walkers:
            if self is not walker:
                if abs(walker.x - self.x) < self.radius * 2 and abs(walker.y - self.y) < self.radius * 2:
                    return True
        return False

    def move(self):
        global files
        self.x += random.random() * self.randomOff - self.randomOff / 2
        self.y += self.speed

        if self.y >= height / 2 or self.collide():
            self.moving = False
            if self.y > self.radius:
                walker = Walker(width / 2 + width / 2 - self.x, self.y, False)
                for i in range(6):
                    spawnRotated(width / 2, height / 2, math.pi / 3 * i, self.x, self.y)
                    spawnRotated(width / 2, height / 2, math.pi / 3 * i, walker.x, walker.y)
                walkers.append(Walker(width / 2, 0, True))
                walkers.append(walker)
            else:
                files += 1
                filename = 'snowflake' + str(files) + '.png'
                pygame.image.save(screen, filename)



    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), [int(self.x), int(self.y)], self.radius)

walkers = [Walker(width / 2, 0, True)]

def spawnRotated(cx, cy, angle, x, y):
    s = math.sin(angle)
    c = math.cos(angle)

    px = x - cx
    py = y - cy

    xnew = px * c - py * s
    ynew = px * s + py * c

    px = xnew + cx
    py = ynew + cy

    walkers.append(Walker(px, py, False))

def update():
    global walkers
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                walkers = [Walker(width / 2, 0, True)]

    screen.fill((0, 0, 0))

    for walker in walkers:
        if walker.moving:
            walker.move()

        else:
            walker.draw()

def main():
    while True:
        update()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
