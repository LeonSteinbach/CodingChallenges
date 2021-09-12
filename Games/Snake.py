import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 7
fpsClock = pygame.time.Clock()

width, height = 300, 300
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((width, height))

fieldSize = 20

class Snake:
    def __init__(self):
        self.x = math.floor(int((width / 2) / fieldSize)) * fieldSize
        self.y = math.floor(int((height / 2) / fieldSize)) * fieldSize
        self.tail = []
        self.total = 1
        self.dir = 0

    def update(self):
        if self.total > 0:
            if self.total == len(self.tail) and self.tail != []:
                del self.tail[0]
            self.tail.append([self.x, self.y])

        if len(self.tail) > 0:
            self.tail[self.total-1][0] = self.x
            self.tail[self.total-1][1] = self.y

        if self.dir == 0: self.y -= fieldSize
        if self.dir == 1: self.x += fieldSize
        if self.dir == 2: self.y += fieldSize
        if self.dir == 3: self.x -= fieldSize

        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            self.x = math.floor(int((width / 2) / fieldSize)) * fieldSize
            self.y = math.floor(int((height / 2) / fieldSize)) * fieldSize
            self.tail = []
            self.total = 1
            self.dir = 0

        for i in range(len(self.tail) - 1):
            if self.x == self.tail[i][0] and self.y == self.tail[i][1]:
                self.total = 1
                self.tail = []
                break

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, fieldSize, fieldSize])
        for t in self.tail:
            pygame.draw.rect(screen, (255, 255, 255), [t[0], t[1], fieldSize, fieldSize])

snake = Snake()

class Food:
    def __init__(self):
        self.x = math.floor(int(random.randint(0, width) / fieldSize)) * fieldSize
        self.y = math.floor(int(random.randint(0, height) / fieldSize)) * fieldSize

    def update(self):
        if self.x == snake.x and self.y == snake.y:
            self.x = math.floor(int(random.randint(0, width) / fieldSize)) * fieldSize
            self.y = math.floor(int(random.randint(0, height) / fieldSize)) * fieldSize

            snake.total += 1

    def draw(self):
        pygame.draw.rect(screen, (255, 155, 155), [self.x, self.y, fieldSize, fieldSize])

food = Food()

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                snake.dir = 0
            if event.key == pygame.K_d:
                snake.dir = 1
            if event.key == pygame.K_s:
                snake.dir = 2
            if event.key == pygame.K_a:
                snake.dir = 3

    food.update()
    snake.update()

def draw():
    screen.fill((0, 0, 0))

    snake.draw()
    food.draw()

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
