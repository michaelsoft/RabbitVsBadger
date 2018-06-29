import pygame

class Player:
    __step = 5
    
    def __init__(self, screen):
        self.__screen = screen
        self.__img = pygame.image.load("resources/images/dude.png")
        self.__pos = [100,100]
    
    @property
    def img(self):
        return self.__img

    @property
    def pos(self):
        return self.__pos
    
    def draw(self):
        self.__screen.blit(self.__img, self.__pos)

    def moveUp(self):
        self.__pos[1] -= Player.__step; 
        if self.__pos[1] <=0:
           self.__pos[1] = 0 
    
    def moveDown(self):
        self.__pos[1] += Player.__step; 
        maxY = self.__screen.get_height() - self.__img.get_height()
        if self.__pos[1] > maxY:
            self.__pos[1] = maxY 

    def moveLeft(self):
        self.__pos[0] -= Player.__step; 
        if self.__pos[0] <=0:
           self.__pos[0] = 0 
    
    def moveRight(self):
        self.__pos[0] += Player.__step; 
        maxX = self.__screen.get_width() - self.__img.get_width()
        if self.__pos[0] > maxX:
            self.__pos[0] = maxX 
   



