import pygame

class Badger:
    __badgerImg1 = pygame.image.load("resources/images/badguy.png")

    def __init__(self, pos):
        self.__img = Badger.__badgerImg1
        self.__pos = pos
    
    @property
    def img(self):
        return self.__img

    @property
    def pos(self):
        return self.__pos

    def move(self):
        pass


