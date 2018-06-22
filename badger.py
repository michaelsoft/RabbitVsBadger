import pygame

class Badger:
    __badgerImg1 = pygame.image.load("resources/images/badguy.png")
    __badgers = []

    def __init__(self, screen, pos):
        self.__img = Badger.__badgerImg1
        self.__pos = pos
        self.__screen = screen

    def move(self):
        pass

    def draw(self):
        self.__screen.blit(self.__img, self.__pos)
        

if __name__ == '__main__':
    pass
