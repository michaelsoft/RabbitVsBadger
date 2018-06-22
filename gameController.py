import pygame
from pygame.locals import *
from player import Player
from badger import Badger
from badgerManager import BadgerManager

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
player = Player(screen)
badgerManager = BadgerManager(screen)
badgerManager.newBadger()
badgerManager.newBadger()
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
playerActions = [False, False, False, False]

while 1:
    screen.fill(0)

    for x in range((int)(width/grass.get_width()+1)):
       for y in range((int)(height/grass.get_height()+1)):
          screen.blit(grass,(x*100,y*100))

    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))

    player.draw()
    badgerManager.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
        
        if event.type==pygame.KEYDOWN:
            if event.key==K_w:
                playerActions[0] = True
            elif event.key==K_s:
                playerActions[1] = True
            elif event.key==K_a:
                playerActions[2] = True
            elif event.key==K_d:
                playerActions[3] = True
    
        if event.type==pygame.KEYUP:
            if event.key==K_w:
                playerActions[0] = False
            elif event.key==K_s:
                playerActions[1] = False
            elif event.key==K_a:
                playerActions[2] = False
            elif event.key==K_d:
                playerActions[3] = False

    if playerActions[0]:
        player.moveUp()
    elif playerActions[1]:
        player.moveDown()
    elif playerActions[2]:
        player.moveLeft()
    elif playerActions[3]:
        player.moveRight()