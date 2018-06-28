import pygame
from arrow import Arrow

class ArrowManager:
    def __init__(self, screen):
        self.__screen = screen
        self.__arrows = []
        self.__currentArrow = None
    
    @property
    def arrows(self):
        return self.__arrows
    
    def loadArrow(self, pos):
        self.__currentArrow = Arrow(pos,self.__screen)
        self.__arrows.append(self.__currentArrow)
    
    def shoot(self):
        if self.__currentArrow != None:
            self.__currentArrow.moving = True

    def moveArrows(self):
        for arrow in self.__arrows:
            if arrow.moving:
                arrow.move()
        
        index = 0
        for arrow in self.__arrows:
            if arrow.isOutOfScreen():
                self.__arrows.pop(index)

    def drawArrows(self):
        for arrow in self.__arrows:
            arrow.draw()



