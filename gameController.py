import pygame
import random
from pygame.locals import *
from player import Player
from badger import Badger
from badgerManager import BadgerManager
from arrow import Arrow

pygame.init()
score = 0
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
player = Player(screen)
arrow = None
arrows = []
badgers = []
newBadgerTimer = 100

playerActions = [False, False, False, False]

def loadArrow():
    x = player.pos[0] + player.img.get_width()
    y = player.pos[1] + (int)(player.img.get_height()/2)
    arrow = Arrow(screen,[x,y])
    return arrow
    
def shoot():
    if arrow != None:
        arrow.moving = True

def moveArrows():
    for arrow in arrows:
        if arrow.moving:
            arrow.move()

def drawArrows():
    index = 0
    for arrow in arrows:
        if arrow.isOutOfScreen:
            arrows.pop(index)
    for arrow in arrows:
        arrow.draw()

def checkShotArrows(arrows, badgers):
    i = 0
    j = 0
    #print (len(badgers))
    for arrow in arrows:
        for badger in badgers:
            if arrow.isShotBadger(badger):
                #score += 1
                arrows.pop(i)
                badgers.pop(j)
                break
            j += 1
        i += 1

def newBadger():
    newBadgerTimer = 1
    y = random.randint(50, 450)
    pos = [540, y]
    badger = Badger(screen, pos)
    badgers.append(badger)

def drawBadgers():
    for badger in badgers:
        badger.draw()

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
    drawBadgers()
    drawArrows()

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
            elif event.key==K_SPACE:
                arrow = loadArrow()
                arrows.append(arrow)
    
        if event.type==pygame.KEYUP:
            if event.key==K_w:
                playerActions[0] = False
            elif event.key==K_s:
                playerActions[1] = False
            elif event.key==K_a:
                playerActions[2] = False
            elif event.key==K_d:
                playerActions[3] = False
            elif event.key==K_SPACE:
                shoot()

    if playerActions[0]:
        player.moveUp()
    elif playerActions[1]:
        player.moveDown()
    elif playerActions[2]:
        player.moveLeft()
    elif playerActions[3]:
        player.moveRight()
    
    if newBadgerTimer >= 100:
        newBadgerTimer = 1
        newBadger()
    else:
        newBadgerTimer += 1

    checkShotArrows(arrows, badgers)
    moveArrows()



