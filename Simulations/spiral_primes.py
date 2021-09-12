from numpy import zeros
from math import sqrt, ceil
import sys
import pygame
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 800, 800
pygame.display.set_caption('Spiral Primes')
screen = pygame.display.set_mode((width, height))


def get_primes(n: int) -> list:
    if n <= 1:
        return []
    my_primes = [2]
    for i in range(3, n+1):
        for c in my_primes:
            if i % c == 0:
                break
        else:
            my_primes.append(i)
    return my_primes


def spiral_primes(size: int):
    if size % 2 == 0:
        size -= 1
    point = [size // 2 - 1, size // 2]
    
    array = zeros([size, size])
    array[point[0], point[1]] = 1
    
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    l = 1
    d = 0
    counter = 0
    counter2 = 0
    
    for i in range(1, size ** 2 + 1):
        point[0] += dirs[d][0]
        point[1] += dirs[d][1]
        
        if counter2 == 2:
            counter2 = 0
            l += 1
        if counter == l:
            if d < 3:
                d += 1
            else:
                d = 0
            counter = 0
            counter2 += 1
        
        counter += 1
        if i in primes:
            array[point[0], point[1]] = 1
    return array


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def draw():
    screen.fill((0, 0, 0))
    for y in range(size-1):
        for x in range(size-1):
            if array[x, y] == 1:
                pygame.draw.circle(screen, (255, 255, 255), [x * tileSize, y * tileSize], int(tileSize / 2))


def main():
    draw()
    
    while True:
        update()

        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    size = 200
    primes = get_primes(size ** 2)
    print(len(primes))
    array = spiral_primes(size)
    tileSize = width // size
    main()
