from badger import Badger
import random

class BadgerManager:
    __maxCount = 3
    def __init__(self, screen):
        self.__screen = screen
        self.__badgers = []
        self.__newBadgerTimer = 100
    
    def drawBadgers(self):
        for badger in self.__badgers:
            badger.draw()

    def moveBadgers(self):
        index = 0
        for badger in self.__badgers:
            badger.move()
            if badger.isOutOfScreen():
                self.__badgers.remove(index)
            index += 1
        


    @property
    def badgers(self):
        return self.__badgers

    def __newBadger(self):
        y = random.randint(50, 450)
        pos = [540, y]
        badger = Badger(pos, self.__screen)
        self.__badgers.append(badger)

    def OnTimeTicked(self):
        if self.__newBadgerTimer >= 100:
            self.__newBadgerTimer = 1
            if len(self.__badgers) < BadgerManager.__maxCount:
               self.__newBadger()
        else:
            self.__newBadgerTimer += 1
            
        self.moveBadgers()
    
    def removeBadger(self,index):
        self.__badgers.remove(index)
    

