import settings 
import pygame
from abc import ABC, abstractmethod



class BlockModel(ABC):

    def __init__(self, position):
        super().__init__()
        self._position=position
        self._lives=None
        self._block_image = None
        self._im = None
        self._width = None
        self._height =None
        self._hitbox = None
       
        

#Getter attributo
    # MUST IMPLEMENT POSITION
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    
#MUST IMPLEMENT LIVES
    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        self._lives = self._lives


#MUST IMPLEMENT BLOCK_IMAGE
    @property
    def block_image(self):
        return self._block_image

    @block_image.setter
    def block_image(self, block_image):
        self._block_image = block_image


#MUST IMPLEMENT IM
    @property
    def im(self):
        return self._im

    @im.setter
    def im(self, im):
        self._im = im


#MUST IMPLEMENT WIDTH
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width


#MUST IMPLEMENT HEIGHT
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def hitbox(self):
        return self._hitbox

    @hitbox.setter
    def hitbox(self, hitbox):
        self._hitbox = hitbox

    @abstractmethod
    def updatePos(self):
        pass

    @abstractmethod
    def hit(self):
        self._lives -=1
        return self._lives

