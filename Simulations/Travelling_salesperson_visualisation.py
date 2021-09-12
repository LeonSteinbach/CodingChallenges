import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 20)

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1000, 1000
pygame.display.set_caption("Travelling Salesperson Visualisation")
screen = pygame.display.set_mode((width, height))

def nextPermutation(array):
    i = len(array)-1
    while i>0 and array[i-1]>=array[i]:
        i -= 1

    if i<=0:
        return False

    j = len(array)-1
    while array[j]<=array[i-1]:
        j -= 1

    temp = array[i-1]
    array[i-1] = array[j]
    array[j] = temp

    j = len(array)-1
    while i<j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i += 1
        j -= 1

    return True

class Node:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), [self.x, self.y], 10)

n = 8

nodes = []
for i in range(n):
    nodes.append(Node())

arr = [i for i in range(n)]
mutations = [i for i in range(n)]
while nextPermutation(arr):
    mutations += arr

mutations = [mutations[i:i+n] for i in range(0, len(mutations), n)]

dists = []
shortestI = 0

def run():
    global shortestI
    for i in range(len(mutations)):
        dist = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        textsurface0 = myfont.render("Progress [%]:  " + str(round(i / len(mutations) * 100, 2)), False, (255, 255, 255))
        screen.blit(textsurface0, (10, 10))
        textsurface1 = myfont.render("n = " + str(n) + "! = " + str(math.factorial(n)), False, (255, 255, 255))
        screen.blit(textsurface1, (10, 35))

        for node in nodes:
            node.draw()

        for c in range(n-1):
            dist += math.hypot(nodes[mutations[i][c+1]].x - nodes[mutations[i][c]].x, nodes[mutations[i][c+1]].y - nodes[mutations[i][c]].y)
            pygame.draw.line(screen, (50, 50, 50), [nodes[mutations[i][c]].x, nodes[mutations[i][c]].y], [nodes[mutations[i][c+1]].x, nodes[mutations[i][c+1]].y], 1)

        if len(dists) > 0 and dist < min(dists):
            shortestI = i

        for c in range(n-1):
            pygame.draw.line(screen, (155, 255, 155), [nodes[mutations[shortestI][c]].x, nodes[mutations[shortestI][c]].y], [nodes[mutations[shortestI][c+1]].x, nodes[mutations[shortestI][c+1]].y], 5)

        dists.append(dist)

        pygame.display.flip()

    print("finished")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    run()

        for node in nodes:
            node.draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
