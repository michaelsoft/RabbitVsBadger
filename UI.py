import pygame
<<<<<<< HEAD
from UI import *
=======
>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e

class UI:
    __grassImg = pygame.image.load("resources/images/grass.png")

    def __init__(self):
        self.__player = None
        self.__arrows = []
        self.__badgers = []
        self.__castles = []

    def setScreen(self, width, height):
        self.__screen = pygame.display.set_mode((width, height))
    
    def registerPlayer(self, player):
        self.__player = player
    
    def registerCastles(self, castles):
        self.__castles = castles

    def registerArrows(self, arrows):
        self.__arrows = arrows

    def registerBadgers(self, badgers):
        self.__badgers = badgers
    
    def drawObjects(self):
        self.__screen.fill(0)
        self.__drawBackground()
        self.__drawPlayer()
        self.__drawArrows()
        self.__drawBadgers()
        pygame.display.flip()

    def isOutOfScreen(self, obj):
        if obj.pos[0] < 0:
           return True
        elif obj.pos[0] + obj.img.get_width() > self.__screen.get_width():
           return True
        elif obj.pos[1] < 0:
           return True
        elif obj.pos[1] + obj.img.get_height() > self.__screen.get_height():
           return True
        else:
           return False

    def __drawBackground(self):
        for x in range((int)(self.__screen.get_width()/UI.__grassImg.get_width()+1)):
            for y in range((int)(self.__screen.get_height()/UI.__grassImg.get_height()+1)):
               self.__screen.blit(UI.__grassImg,(x*100,y*100))

    def __drawCastles(self):
        for castle in self.__castles:
            self.__drawObject(castle)

    def __drawPlayer(self):
        self.__drawObject(self.__player)
    
    def __drawArrows(self):
        for arrow in self.__arrows:
            self.__drawObject(arrow)

    def __drawBadgers(self):
        for badger in self.__badgers:
            self.__drawObject(badger)

    def __drawObject(self, obj):
        self.__screen.blit(obj.img, obj.pos)

theUI = UI() #Let UI be singleton