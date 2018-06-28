import pygame

class Castle:
    __castleImg = pygame.image.load("resources/images/castle.png")
    __pos = []

    def __init__(self, pos, screen):
        self.__screen = screen
        self.__img = Castle.__castleImg
        self.__pos = pos
    
    @property
    def img(self):
        return self.__img

    @property
    def pos(self):
        return self.__pos

    def draw(self):
        self.__screen.blit(self.__img, self.__pos)
    
class CastleManager:
    def __init__(self, screen):
        self.__screen = screen
        self.__castles = []
    
    @property
    def castles(self):
        return self.__castles

    def initCastles(self):
        castle1 = Castle((0,30),self.__screen)
        self.__castles.append(castle1)
        castle2 = Castle((0,135),self.__screen)
        self.__castles.append(castle2)
        castle3 = Castle((0,240),self.__screen)
        self.__castles.append(castle3)
        castle4 = Castle((0,345),self.__screen)
        self.__castles.append(castle4)
   
    def drawCastles(self):
        for castle in self.__castles:
           castle.draw()


