import pygame
from pygame.locals import *
from player import Player
from badger import Badger

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
player = Player(screen)
badger = Badger(screen)
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

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
    badger.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
        
        if event.type==pygame.KEYDOWN:
            if event.key==K_w:
                player.moveUp()
            elif event.key==K_s:
                player.moveDown()
            elif event.key==K_a:
                player.moveLeft()
            elif event.key==K_d:
                player.moveRight()