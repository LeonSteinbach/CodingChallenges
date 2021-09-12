import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1400, 800
pygame.display.set_caption("Attraction Repulsion")
screen = pygame.display.set_mode((width, height))

repulsion = False
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

class Attractor:
    def __init__(self, position):
        self.position = position

        self.radius = 8

    def draw(self):
        pygame.draw.circle(screen, (155, 55, 55), self.position, self.radius)

attractors = []

class Ball:
    def __init__(self, position, vector):
        self.position = position
        self.vector = vector

        self.acceleration = [0, 0]
        self.radius = 2
        self.speed = 1

        self.s = pygame.Surface((self.radius, self.radius), pygame.SRCALPHA)

    def update(self):
        global repulsion
        for attractor in attractors:
            dist = math.hypot(attractor.position[0] - self.position[0], attractor.position[1] - self.position[1]) + 1
            self.acceleration = [self.position[0] - attractor.position[0], self.position[1] - attractor.position[1]]

            if repulsion:
                if dist > 100:
                    self.acceleration[0] /= -math.sqrt(self.position[0] ** 2 + self.position[1] ** 2)
                    self.acceleration[1] /= -math.sqrt(self.position[0] ** 2 + self.position[1] ** 2)
                else:
                    self.acceleration[0] /= math.sqrt(self.position[0] ** 2 + self.position[1] ** 2)
                    self.acceleration[1] /= math.sqrt(self.position[0] ** 2 + self.position[1] ** 2)
            else:
                self.acceleration[0] /= -math.sqrt(self.position[0] ** 2 + self.position[1] ** 2)
                self.acceleration[1] /= -math.sqrt(self.position[0] ** 2 + self.position[1] ** 2)

            self.acceleration[0] /= dist / self.speed
            self.acceleration[1] /= dist / self.speed

            self.vector[0] += self.acceleration[0]
            self.vector[1] += self.acceleration[1]

        self.position[0] += self.vector[0]
        self.position[1] += self.vector[1]

    def draw(self):
        global r, g, b
        r += 1
        g -= 1
        b += 1
        if r > 255: r = 0
        if g < 0: g = 255
        if b > 255: b = 0

        pygame.draw.circle(self.s, (r, g, b, 50), [0, 0], self.radius)
        screen.blit(self.s, [int(self.position[0]), int(self.position[1])])

balls = []
balls.append(Ball([width / 2, height / 2], [0.01, 0.01]))

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                attractors.append(Attractor(pygame.mouse.get_pos()))

    if pygame.mouse.get_pressed() == (0, 0, 1):
        pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 5)

    for ball in balls:
        ball.update()

def draw():
    #screen.fill((0, 0, 0))
    #for attractor in attractors:
    #    attractor.draw()

    for ball in balls:
        ball.draw()

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
