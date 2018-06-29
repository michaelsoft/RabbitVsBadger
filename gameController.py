import pygame
import random
from pygame.locals import *

from player import *
from badgerManager import BadgerManager
from arrowManager import ArrowManager
from castle import CastleManager

score = 0

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

grass = pygame.image.load("resources/images/grass.png")


player = Player(screen)
castleManager = CastleManager(screen)
castleManager.initCastles()
badgerManager = BadgerManager(screen)
arrowManager = ArrowManager(screen)

playerActions = [False, False, False, False]

scoreFont = pygame.font.Font(None, 24)
scoreMsg = "Score: " + str(score)
scoreText = scoreFont.render(scoreMsg.zfill(2), True, (0,0,0) )
scoreTextRect = scoreText.get_rect()
scoreTextRect.topright = (635, 5)

while 1:
    badgerManager.OnTimeTicked()

    screen.fill(0)

    screen.blit(scoreText, scoreTextRect)

    for x in range((int)(screen.get_width()/grass.get_width()+1)):
      for y in range((int)(screen.get_height()/grass.get_height()+1)):
        screen.blit(grass,(x*100,y*100))
    
    castleManager.drawCastles()
    player.draw()
    badgerManager.drawBadgers()
    arrowManager.drawArrows()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                playerActions[0] = True
            elif event.key==pygame.K_s:
                playerActions[1] = True
            elif event.key==pygame.K_a:
                playerActions[2] = True
            elif event.key==pygame.K_d:
                playerActions[3] = True
            elif event.key==pygame.K_SPACE:
                x = player.pos[0] + player.img.get_width()
                y = player.pos[1] + (int)(player.img.get_height()/2)
                arrowManager.loadArrow([x,y])
    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                playerActions[0] = False
            elif event.key==pygame.K_s:
                playerActions[1] = False
            elif event.key==pygame.K_a:
                playerActions[2] = False
            elif event.key==pygame.K_d:
                playerActions[3] = False
            elif event.key==pygame.K_SPACE:
                arrowManager.shoot()

    if playerActions[0]:
        player.moveUp()
    elif playerActions[1]:
        player.moveDown()
    elif playerActions[2]:
        player.moveLeft()
    elif playerActions[3]:
        player.moveRight()
    
    arrowManager.moveArrows()
    shotBadgers = arrowManager.checkShotArrows(badgerManager.badgers)
    score += shotBadgers

def checkShotArrows(arrows, badgers):
    i = 0
    for arrow in arrows:
        j = 0
        for badger in badgers:
            if arrow.isShotBadger(badger):
                #score += 1
                arrows.pop(i)
                badgers.pop(j)
                #break
            j += 1
        i += 1


