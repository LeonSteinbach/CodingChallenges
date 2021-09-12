import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1000, 1000
pygame.display.set_caption("Sorting Visualization")
screen = pygame.display.set_mode((width, height))

array = []
numbers = [i for i in range(0, 1000)]
while len(numbers) > 0:
    randI = random.randint(0, len(numbers) - 1)
    array.append(numbers[randI])
    del numbers[randI]

sorted = False
algorithmus = "bubble"
lo = 0
hi = len(array) - 1

running = False

def map(x, i1, i2, o1, o2):
    return o1 + ((o2 - o1) / (i2 - i1)) * (x - i1)

def quickSort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quickSort(a, lo, p - 1)
        quickSort(a, p + 1, hi)

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi - 1):
        if a[j] < pivot:
            if i != j:
                temp0 = a[j]
                a[j] = a[i]
                a[i] = temp0
            i += 1
    temp1 = a[hi]
    a[hi] = a[i]
    a[i] = temp1
    return i

def update():
    global running, lo, hi
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                running = True

    if running:
        if algorithmus == "bubble":
            sorted = False
            if not sorted:
                sorted = True
                for i in range(len(array) - 1):
                    if array[i] > array[i + 1]:
                        temp = array[i]
                        array[i] = array[i + 1]
                        array[i + 1] = temp
                        sorted = False

        elif algorithmus == "quick":
            if lo < hi:
                p = partition(array, lo, hi)
                quickSort(array, lo, p - 1)
                quickSort(array, p + 1, hi)

def draw():
    screen.fill((0, 0, 0))

    for i in range(len(array) - 1):
        w = int(width / len(array))
        h = map(array[i], 0, len(array), 0, height)
        pygame.draw.rect(screen, (255, 255, 255), [i * w, height - h, w, h])

def main():
    while True:
        update()
        draw()

        pygame.display.flip()
        fpsClock.tick(fps)

main()
