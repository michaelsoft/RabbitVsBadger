import pygame
import random
from pygame.locals import *

from player import Player
from badgerManager import BadgerManager
from arrowManager import ArrowManager
from UI import theUI
from castle import CastleManager

class GameController:
    __score = 0

    @staticmethod
    def main():
        pygame.init()
        
        width, height = 640, 480
        theUI.setScreen(width, height)

        castleManager = CastleManager()
        player = thePlayer
        badgerManager = BadgerManager()
        arrowManager = ArrowManager()

        theUI.registerCastles(castleManager.castles)
        theUI.registerPlayer(player)
        theUI.registerArrows(arrowManager.arrows)
        theUI.registerBadgers(badgerManager.badgers)

        playerActions = [False, False, False, False]

        while 1:
            
            theUI.drawObjects()

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
                        x = player.pos[0] + player.img.get_width()
                        y = player.pos[1] + (int)(player.img.get_height()/2)
                        arrowManager.loadArrow([x,y])
            
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
                        arrowManager.shoot()

            if playerActions[0]:
                player.moveUp()
            elif playerActions[1]:
                player.moveDown()
            elif playerActions[2]:
                player.moveLeft()
            elif playerActions[3]:
                player.moveRight()
            

            GameController.checkShotArrows(arrowManager.arrows, badgerManager.badgers)
            arrowManager.moveArrows()

    @staticmethod
    def checkShotArrows(arrows, badgers):
        i = 0
        j = 0
        for arrow in arrows:
            for badger in badgers:
                if arrow.isShotBadger(badger):
                    GameController.__score += 1
                    arrows.pop(i)
                    badgers.pop(j)
                    break
                j += 1
            i += 1

if __name__ == '__main__':
    GameController.main()
