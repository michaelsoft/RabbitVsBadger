import pygame

class Player:
    step = 5

    def __init__(self,screen):
        self.player = pygame.image.load("resources/images/dude.png")
        self.playerpos = [100,100]
        self.screen = screen

    def moveUp(self):
        self.playerpos[1] -= Player.step; 
    
    def moveDown(self):
        self.playerpos[1] += Player.step; 

    def moveLeft(self):
        self.playerpos[0] -= Player.step; 
    
    def moveRight(self):
        self.playerpos[0] += Player.step; 
   
    def draw(self):
        self.screen.blit(self.player, self.playerpos)