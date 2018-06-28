from badger import Badger
import random

class BadgerManager:
    def __init__(self):
        self.__badgers = []
        self.__newBadgerTimer = 100
    
    def drawBadgers(self):
        for badger in self.__badgers:
            badger.draw()

    @property
    def badgers(self):
        return self.__badgers

    def __newBadger(self):
        y = random.randint(50, 450)
        pos = [540, y]
        badger = Badger(pos)
        self.__badgers.append(badger)

    def OnTimeTicked(self):
        if self.__newBadgerTimer >= 100:
            self.__newBadgerTimer = 1
            self.__newBadger()
        else:
            self.__newBadgerTimer += 1
    
    def removeBadger(self,index):
        self.__badgers.remove(index)
    

