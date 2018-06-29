import pygame

class Badger:
    __badgerImg1 = pygame.image.load("resources/images/badguy.png")
    __step = 2

    def __init__(self, pos, screen):
        self.__screen = screen
        self.__img = Badger.__badgerImg1
        self.__pos = pos
    
    @property
    def img(self):
        return self.__img

    @property
    def pos(self):
        return self.__pos
    
    def draw(self):
        self.__screen.blit(self.__img, self.__pos)

    def move(self):
        self.__pos[0] -= Badger.__step
    
    def isHitCastle(self, castle):
        badgerRect = pygame.Rect(self.__img.get_rect())
        badgerRect.left = self.__pos[0]
        badgerRect.top = self.__pos[1]

        castleRect = pygame.Rect(castle.img.get_rect())
        castleRect.left = castle.pos[0]
        castleRect.top = castle.pos[1]

        if badgerRect.colliderect(castleRect):
           return True
        else:
           return False

    def isOutOfScreen(self):
        if self.__pos[0] < 0:
           return True
        elif self.__pos[0] + self.__img.get_width() > self.__screen.get_width():
           return True
        elif self.__pos[1] < 0:
           return True
        elif self.__pos[1] + self.__img.get_height() > self.__screen.get_height():
           return True
        else:
           return False



