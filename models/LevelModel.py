import settings
from random import randint
from models.blocks.Block1 import Block1
from models.blocks.Block2 import Block2
from models.blocks.Block3 import Block3
import utils.levels as levels


class LevelModel:

    def __init__(self):
        self.__blocks = levels.builder(0)
        self.__levelCount=0
#Getter attributo
    

    @property
    def blocks(self):
        return self.__blocks

    @property
    def levelCount(self):
        return self.__levelCount

    def next(self):
        self.__levelCount +=1
        self.__blocks = levels.builder(self.__levelCount)




