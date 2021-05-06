import pygame
import settings 
from PIL import Image
from abc import ABC, abstractmethod 
from models.BlockModel import BlockModel


#######????????????????????????????????????????
class Block3(BlockModel):

    def __init__(self,position_):
        super().__init__(position_)
        self._lives=2
        self._block_image = pygame.image.load('./utils/blocks/brick3.png')
        self._im = Image.open('./utils/blocks/brick3.png')
        self._width = self._im.size[0]
        self._height =self._im.size[1]
        self._hitbox = pygame.Rect(self._position['x'],
                                    self._position['y'],
                                    self._width,
                                    self._height)
    
    def updatePos(self):
        self.hitbox = pygame.Rect(self._position['x'],
                                    self._position['y'], 
                                    self._width, 
                                    self._height)

    def hit(self):
        return super().hit()
        

    
    
    
    
    

    

    

    
    

    

   

    
        
        