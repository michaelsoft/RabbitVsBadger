import pygame
from pygame.locals import *
from player import Player

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
player = Player(screen)

while 1:
    screen.fill(0)
    player.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)