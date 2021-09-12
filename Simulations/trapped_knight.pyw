import sys
import pygame
import numpy
from pygame.locals import *

pygame.init()

fps = 1000
fpsClock = pygame.time.Clock()

width, height = 1000, 1000
pygame.display.set_caption('Trapped Knight')
screen = pygame.display.set_mode((width, height))

Arial = pygame.font.SysFont('Arial', 10)


def create_array():
    global size, array, visited, checked, path, tile_size
    size = 65
    tile_size = width // size
    point = [size // 2 - 1, size // 2]

    visited = []
    checked = []
    path = []
    array = numpy.zeros([size, size])
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
        array[point[0], point[1]] = i


def walk():
    pos = [size // 2 - 2, size // 2 - 1]
    dirs = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    min_pos = pos
    while min_pos is not None:
        min_pos = None
        for d in dirs:
            new_pos = [pos[0]+d[0], pos[1]+d[1]]
            if new_pos[0] < 0 or new_pos[0] > size-1 or new_pos[1] < 0 or new_pos[1] > size-1:
                continue
            if new_pos not in path:
                if min_pos is None:
                    min_pos = new_pos
                    continue
                if array[new_pos[0], new_pos[1]] < array[min_pos[0], min_pos[1]]:
                    min_pos = new_pos
                checked.append(new_pos)
        pos = min_pos
        path.append(min_pos)

    # print([int(array[p[0], p[1]]) for p in path if p])


def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass


def draw():
    screen.fill((255, 255, 255))
    color = 0
    for i in range(1, len(path)-1):
        color += 1.0 / len(path) * 255
        pygame.draw.line(screen, (int(color), int(color), 255-int(color)),
                         [path[i-1][0] * tile_size + tile_size/2, path[i-1][1] * tile_size + tile_size/2],
                         [path[i][0] * tile_size + tile_size/2, path[i][1] * tile_size + tile_size/2], 2)

    for pos in checked:
        if pos not in path:
            pygame.draw.rect(screen, (255, 100, 100), [pos[0] * tile_size + int(tile_size/2), pos[1] * tile_size + int(tile_size/2), 2, 2])
    pygame.draw.circle(screen, (0, 0, 0), [path[-2][0] * tile_size + int(tile_size/2), path[-2][1] * tile_size + int(tile_size/2)], 2)


def main():
    while True:
        update()

        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    create_array()
    walk()
    draw()
    main()
