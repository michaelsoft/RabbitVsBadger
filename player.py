import pygame
from arrow import Arrow

class Player:
    __step = 5
    __arrowStep = 5
    
    def __init__(self,screen):
        self.__playerImg = pygame.image.load("resources/images/dude.png")
        self.__playerpos = [100,100]
        self.__screen = screen
        self.__arrows = []
        self.__arrow = None

    def moveUp(self):
        self.__playerpos[1] -= Player.__step; 
        if self.__playerpos[1] <=0:
           self.__playerpos[1] = 0 
    
    def moveDown(self):
        self.__playerpos[1] += Player.__step; 
        maxY = self.__screen.get_height() - self.__playerImg.get_height()
        if self.__playerpos[1] > maxY:
           self.__playerpos[1] = maxY 

    def moveLeft(self):
        self.__playerpos[0] -= Player.__step; 
        if self.__playerpos[0] <=0:
           self.__playerpos[0] = 0 
    
    def moveRight(self):
        self.__playerpos[0] += Player.__step; 
        maxX = self.__screen.get_width() - self.__playerImg.get_width()
        if self.__playerpos[0] > maxX:
           self.__playerpos[0] = maxX 
   
    def draw(self):
        self.__screen.blit(self.__playerImg, self.__playerpos)
        self.__moveArrow()
        for arrow in self.__arrows:
            arrow.draw()
    
    
    def loadArrow(self):
        x = self.__playerpos[0] + self.__playerImg.get_width()
        y = self.__playerpos[1] + (int)(self.__playerImg.get_height()/2)
        arrow = Arrow(self.__screen,[x,y])
        self.__arrow = arrow
        self.__arrows.append(arrow)
        
    def shoot(self):
        self.__arrow.moving = True

    def __moveArrow(self):
        for arrow in self.__arrows:
            if arrow.moving:
                arrow.move()
