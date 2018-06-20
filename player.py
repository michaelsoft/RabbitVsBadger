import pygame

class Player:
    def __init__(self,screen):
        self.player = pygame.image.load("resources/images/dude.png")
        self.playerpos = [100,100]
        self.screen = screen
   
    def draw(self):
        self.screen.blit(self.player, self.playerpos)