import settings
from numpy import sign
from PIL import Image
import pygame



class BarModel:
#TODO: IMPLEMENT MOVEMENT ALONG Y
    def __init__(self):
        self.__barSizeBonus = 1
        self.__bar_image = pygame.image.load('./utils/barx25.png')
        self.__im = Image.open('./utils/barx25.png')
        self.__width = self.__im.size[0]*self.__barSizeBonus
        self.__height = self.__im.size[1]*self.__barSizeBonus
        self.__position =  {
            'x': settings.GAME_WIDTH_PIXELS / 2,
            'y': settings.GAME_HEIGHT_PIXELS - self.__height
        }
        
        self.__speed = {
            'x' : 0,
            'y' : 0
        }

        self.__acceleration = {
            'x' : 0,
            'y' : 0
        }        
        self.__width, self.__height =self.__im.size
        self.__hitbox = pygame.Rect(self.__position['x'],
                                    self.__position['y'], 
                                    self.__width,
                                    self.__height)
    



    @property
    def size(self):
        return self.__barSizeBonus


#For now i don't need to get y
    @property
    def speed(self):
        return self.__speed['x']


#For now i don't need to get y
    @property
    def acceleration(self):
        return self.__acceleration['x']


    @property
    def hitbox(self):
        return self.__hitbox


    @property
    def position(self):
        return self.__position


    @property
    def bar_image(self):
        return self.__bar_image
 

    def updatePos(self):
        nextFrict = self.__speed['x'] - sign(self.__speed['x'])
        if self.__acceleration['x']==0:
            if sign(nextFrict) != sign(self.__speed['x']):
                self.__speed['x']=0
            else:
                self.__speed['x']=nextFrict

        nextPos=self.__speed['x'] + self.__position['x']

        if nextPos < 0:
            self.__position['x'] = 0
            self.__acceleration['x'] = -self.__acceleration['x']
            self.__speed['x'] = -self.__speed['x']
        elif nextPos > settings.GAME_WIDTH_PIXELS-self.__width:
            self.__position['x'] = settings.GAME_WIDTH_PIXELS-self.__width
            self.__acceleration['x'] = -self.__acceleration['x']
            self.__speed['x'] = -self.__speed['x']
        else:
            if sign(self.__speed['x']+
                    self.__acceleration['x'])*(
                    self.__speed['x']+
                    self.__acceleration['x'])>=30:
                self.__speed['x']=sign(self.__speed['x'])*30
            else:
                self.__speed['x'] += self.__acceleration['x']
            self.__position['x'] += self.__speed['x']

        self.__hitbox = pygame.Rect(self.__position['x'],
                                    self.__position['y'],
                                    self.__width, 
                                    self.__height)

            
    
    @acceleration.setter
    def acceleration(self, acceleration):
        self.__acceleration['x'] = acceleration
      
         

    
