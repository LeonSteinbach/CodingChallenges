import pygame
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

l = 10
iterations = 0

width, height = l * 64 + l * 2 + 1, l * 64 + l * 2 + 1
pygame.display.set_caption("")
screen = pygame.display.set_mode((width, height))

class Toothpick:
    def __init__(self, x, y, dir):
        if dir == 1:
            self.ax = x - l / 2
            self.bx = x + l / 2
            self.ay = y
            self.by = y
        else:
            self.ax = x
            self.bx = x
            self.ay = y - l / 2
            self.by = y + l / 2

        self.dir = dir
        self.newPick = True
        self.draw()

    def intersects(self, x, y):
        if self.ax == x and self.ay == y:
            return True
        elif self.bx == x and self.by == y:
            return True
        return False

    def createA(self, others):
        available = True
        for other in others:
            if other is not self and other.intersects(self.ax, self.ay):
                available = False
        if available:
            return Toothpick(self.ax, self.ay, self.dir * -1)
        return None

    def createB(self, others):
        available = True
        for other in others:
            if other is not self and other.intersects(self.bx, self.by):
                available = False
                break
        if available:
            return Toothpick(self.bx, self.by, self.dir * -1)
        return None

    def draw(self):
        pygame.draw.line(screen, (255, 255, 255), [self.ax, self.ay], [self.bx, self.by], 1)

picks = [Toothpick(width / 2, height / 2, 1)]

def draw():
    global iterations
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if iterations < 127:
        next = []
        for pick in picks:
            if pick.newPick:
                nextA = pick.createA(picks)
                nextB = pick.createB(picks)
                if nextA != None:
                    next.append(nextA)
                if nextB != None:
                    next.append(nextB)
                pick.newPick = False
        picks.extend(next)

        iterations += 1

def main():
    while True:
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

screen.fill((0, 0, 0))
main()
