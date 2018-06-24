import pygame

class Arrow:
    __arrowImg = pygame.image.load("resources/images/bullet.png")
    __pos = []
    __step = 3

    def __init__(self, screen,pos):
        self.__img = Arrow.__arrowImg
        self.__screen = screen
        self.__pos = pos
        self.__moving = False
    
    @property
    def moving(self):
        return self.__moving

    @moving.setter
    def moving(self, value):
        self.__moving = value

    def move(self):
        self.__pos[0] += Arrow.__step
    
    def draw(self):
        self.__screen.blit(self.__img, self.__pos)

