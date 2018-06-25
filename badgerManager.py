from badger import Badger
import random

class BadgerManager:
    __badgers = []

    def __init__(self,screen):
        self.__screen = screen
    
    def draw(self):
        for badger in self.__badgers:
            badger.draw()

    @property
    def badgers(self):
        return __badgers

    def get_badgerCount(self):
        return BadgerManager.__badgers.count

    def newBadger(self):
        y = random.randint(50, 450)
        pos = [540, y]
        badger = Badger(self.__screen, pos)
        self.__badgers.append(badger)
    
    def removeBadger(badger):
        self.__badgers.remove(badger)

if __name__ == '__main__':
    pass