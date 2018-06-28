import pygame

class Arrow:
    __arrowImg = pygame.image.load("resources/images/bullet.png")
    __pos = []
    __step = 3

    def __init__(self, pos, screen):
        self.__screen = screen
        self.__img = Arrow.__arrowImg
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

    def isShotBadger(self, badger):
        arrowRect = pygame.Rect(self.__arrowImg.get_rect())
        arrowRect.left = self.__pos[0]
        arrowRect.top = self.__pos[1]

        badgerRect = pygame.Rect(badger.img.get_rect())
        badgerRect.left = badger.pos[0]
        badgerRect.top = badger.pos[1]

        if arrowRect.colliderect(badgerRect):
           return True
        else:
           return False
    
    def isOutOfScreen(self):
        if self.__pos[0] <=0:
            return True
        elif self.__pos[0] + self.__img.get_width() >= self.__screen.get_width():
            return True
        elif self.__pos[1] <=0:
            return True
        elif self.__pos[1] + self.__img.get_height() >= self.__screen.get_height():
            return True