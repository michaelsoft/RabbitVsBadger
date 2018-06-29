import pygame

class Arrow:
    __arrowImg = pygame.image.load("resources/images/bullet.png")
    __pos = []
    __step = 3

<<<<<<< HEAD
    def __init__(self, pos, screen):
        self.__screen = screen
=======
    def __init__(self, pos):
>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e
        self.__img = Arrow.__arrowImg
        self.__pos = pos
        self.__moving = False
    
    @property
    def moving(self):
        return self.__moving

    @moving.setter
    def moving(self, value):
        self.__moving = value

<<<<<<< HEAD
    def move(self):
        self.__pos[0] += Arrow.__step
    
    def draw(self):
        self.__screen.blit(self.__img, self.__pos)

=======
>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e
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
    
<<<<<<< HEAD
    def isOutOfScreen(self):
        if self.__pos[0] <=0:
            return True
        elif self.__pos[0] + self.__img.get_width() >= self.__screen.get_width():
            return True
        elif self.__pos[1] <=0:
            return True
        elif self.__pos[1] + self.__img.get_height() >= self.__screen.get_height():
            return True
=======

>>>>>>> 4a76bb3f2f5b156f5e270b3a771d8d55c58fad1e
