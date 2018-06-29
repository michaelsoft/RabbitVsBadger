import pygame
from arrow import Arrow

class ArrowManager:
<<<<<<< HEAD
    def __init__(self, screen):
        self.__screen = screen
=======
    def __init__(self):
>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e
        self.__arrows = []
        self.__currentArrow = None
    
    @property
    def arrows(self):
        return self.__arrows
    
    def loadArrow(self, pos):
<<<<<<< HEAD
        self.__currentArrow = Arrow(pos,self.__screen)
=======
        self.__currentArrow = Arrow(pos)
>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e
        self.__arrows.append(self.__currentArrow)
    
    def shoot(self):
        if self.__currentArrow != None:
            self.__currentArrow.moving = True

    def moveArrows(self):
        for arrow in self.__arrows:
            if arrow.moving:
                arrow.move()
<<<<<<< HEAD
        
        index = 0
        for arrow in self.__arrows:
            if arrow.isOutOfScreen():
                self.__arrows.pop(index)

    def drawArrows(self):
=======

    def drawArrows(self):
        index = 0
        for arrow in self.__arrows:
            if arrow.isOutOfScreen:
                self.__arrows.pop(index)
>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e
        for arrow in self.__arrows:
            arrow.draw()



