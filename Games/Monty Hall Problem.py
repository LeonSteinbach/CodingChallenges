import pygame
import math
import random
import numpy
import time
import socket

''' Initializing '''
__author__ = 'Leon Steinbach'

FPS = 100
gameExit = False
dw = 900
dh = 600
title = "Monty Hall Problem"

pygame.init()
gameDisplay = pygame.display.set_mode((dw, dh))
pygame.display.set_caption(title)
clock = pygame.time.Clock()


''' Images '''


''' Sounds '''


''' Variables '''


''' Colors '''
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
pink = (255, 0, 255)

''' Classes '''
class Door:
    def __init__(self, x, y, choosen, behind, opened):
        self.x = x
        self.y = y
        self.choosen = choosen
        self.behind = behind
        self.opened = opened

    def update(self):
        if not self.opened:
            pygame.draw.rect(gameDisplay, black, (self.x, self.y, 100, 200))
        else:
            pygame.draw.rect(gameDisplay, black, (self.x, self.y, 10, 200))

        if self.choosen:
            pygame.draw.rect(gameDisplay, blue, (self.x+40, self.y + 230, 20, 40))

        if self.opened:
            show_screen_text(str(self.behind), self.x + 30, 300, 30, black)

door1 = Door(100, 100, False, None, False)
door2 = Door(300, 100, False, None, False)
door3 = Door(500, 100, False, None, False)

''' Methods '''
def setBehinds():
    rand = random.randint(1, 3)
    if rand == 1:
        door1.behind = "car"
        door2.behind = "goat"
        door3.behind = "goat"
    if rand == 2:
        door1.behind = "goat"
        door2.behind = "car"
        door3.behind = "goat"
    if rand == 3:
        door1.behind = "goat"
        door2.behind = "goat"
        door3.behind = "car"
setBehinds()


def show_screen_text(msg, text_x, text_y, text_size, color):
    font = pygame.font.SysFont(None, text_size)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (text_x, text_y))


def events():
    global click, keys, cursor, gameExit
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass

            if event.type == pygame.MOUSEBUTTONUP:
                if door1.x < cursor[0] < door1.x + 100:
                    door1.choosen = True
                if door2.x < cursor[0] < door2.x + 100:
                    door2.choosen = True
                if door3.x < cursor[0] < door3.x + 100:
                    door3.choosen = True

                if door1.choosen or door2.choosen or door3.choosen:
                    i = random.randint(1, 2)

                    if door1.choosen and door1.behind == "goat":
                        if door2.behind == "goat":
                            door2.opened = True
                        if door3.behind == "goat":
                            door3.opened = True
                    if door2.choosen and door2.behind == "goat":
                        if door1.behind == "goat":
                            door1.opened = True
                        if door3.behind == "goat":
                            door3.opened = True
                    if door3.choosen and door3.behind == "goat":
                        if door2.behind == "goat":
                            door2.opened = True
                        if door1.behind == "goat":
                            door1.opened = True

                    if door1.choosen and door1.behind == "car":
                        if i == 1:
                            door2.opened = True
                        if i == 2:
                            door3.opened = True
                    if door2.choosen and door2.behind == "car":
                        if i == 1:
                            door1.opened = True
                        if i == 2:
                            door3.opened = True
                    if door3.choosen and door3.behind == "car":
                        if i == 1:
                            door1.opened = True
                        if i == 2:
                            door2.opened = True

    keys = pygame.key.get_pressed()
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


def display():
    gameDisplay.fill(white)

    door1.update()
    door2.update()
    door3.update()

def game_loop():
    global FPS, gameExit, dw, dh
    while not gameExit:
        ''' Actions '''
        events()
        display()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_loop()
