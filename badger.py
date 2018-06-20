import pygame

class Badger:
    badgerImg1 = pygame.image.load("resources/images/badguy.png")

    def __init__(self,screen):
        self.img = Badger.badgerImg1
        self.pos = [540,100]
        self.screen = screen

    def move(self):
        pass

    def draw(self):
        self.screen.blit(self.img, self.pos)
        