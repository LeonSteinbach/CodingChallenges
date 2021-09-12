import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 700, 700
pygame.display.set_caption("Diffusion Limited Aggregation")
screen = pygame.display.set_mode((width, height))

x = 0

class Walker:
    def __init__(self, stable, position, id):
        self.stable = stable
        self.position = position
        self.id = id

        self.speed = 5
        self.radius = 5

    def update(self):
        if not self.stable:
            self.position[0] += random.randint(-self.speed, self.speed)
            self.position[1] += random.randint(-self.speed, self.speed)

        if self.position[0] - self.radius < 0: self.position[0] = self.radius * 2
        if self.position[0] + self.radius > width: self.position[0] = width - self.radius * 2
        if self.position[1] - self.radius < 0: self.position[1] = self.radius * 2
        if self.position[1] + self.radius > height: self.position[0] = height - self.radius * 2

        for walker in walkers:
            if self.id != walker.id and not self.stable and walker.stable:
                if math.hypot(walker.position[0] - self.position[0], walker.position[1] - self.position[1]) < self.radius + walker.radius:
                    self.stable = True
                    walkers.append(Walker(False, [random.randint(0, width), random.randint(0, height)], random.randint(0, 1000000000)))

    def draw(self):
        if self.stable:
            pygame.draw.circle(screen, (200, 0, 50), [int(self.position[0]), int(self.position[1])], self.radius)
        else:
            pygame.draw.circle(screen, (255, 255, 255), [int(self.position[0]), int(self.position[1])], self.radius)

walkers = []
walkers.append(Walker(True, [width / 2, height / 2], -1))
for i in range(200):
    walkers.append(Walker(False, [random.randint(0, width), random.randint(0, height)], i))

def update():
    for walker in walkers:
        walker.update()

def draw():
    global x
    x += 1
    if x % 10 == 0:
        screen.fill((0, 0, 0))
        for walker in walkers:
            walker.draw()

def main():
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

      update()
      draw()

      pygame.display.flip()
      fpsClock.tick(fps)

main()
