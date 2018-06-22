import pygame

class Player:
    __step = 5

    def __init__(self,screen):
        self.__playerImg = pygame.image.load("resources/images/dude.png")
        self.__playerpos = [100,100]
        self.__screen = screen

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
