import settings 
from models.BarModel import BarModel
import pygame
from PIL import Image
from numpy import sign



class BallModel:

    def __init__(self):
        self.__ball_image = pygame.image.load('./utils/ball.png')
        self.__im = Image.open('./utils/ball.png')
        self.__sizeBallBonus = 1
        self.__width = self.__im.size[0]*self.__sizeBallBonus
        self.__height =self.__im.size[1]*self.__sizeBallBonus

        self.__speed = {
            'x' : 15,
            'y' : 15
        }

        self.__position =  {
            'x': 400,
            'y': 400
        }

        self.__topHitbox = pygame.Rect(self.__position['x'],
                                       self.__position['y'] + self.__height/2, 
                                       self.__width*0.3, 
                                       self.__height*0.1)
        self.__botHitbox = pygame.Rect(self.__position['x'],
                                       self.__position['y'] - self.__height/2, 
                                       self.__width*0.3, 
                                       self.__height*0.1)
        self.__leftHitbox = pygame.Rect(self.__position['x'] - self.__width/2,
                                        self.__position['y'] , 
                                        self.__width*0.1, 
                                        self.__height*0.3)
        self.__rightHitbox = pygame.Rect(self.__position['x'] + self.__width/2,
                                         self.__position['y'] , 
                                         self.__width*0.1, 
                                         self.__height*0.3)


#Getter attributo
    @property
    def position(self):
        return self.__position

    @property
    def topHitbox(self):
        return self.__topHitbox

    @property
    def botHitbox(self):
        return self.__botHitbox

    @property
    def leftHitbox(self):
        return self.__leftHitbox

    @property
    def rightHitbox(self):
        return self.__rightHitbox

    @property
    def speed(self):
        return self.__speed

    @property
    def ball_image(self):
        return self.__ball_image

    @speed.setter
    def acceleration(self, speed):
        self.__speed = speed


    @position.setter
    def position(self, position):
        self.__position = position

#todo bounce 
    def bounce(self):
        pass

    def updatePos(self):
        if sign(self.__speed['x'])*self.__speed['x']>20:
            self.__speed['x']=sign(self.__speed['x'])*20

        if self.__position['y'] <= settings.TOP_BAR_HEIGHT_PIXELS:
            self.__position['y'] = settings.TOP_BAR_HEIGHT_PIXELS 
            self.__speed['y'] = -self.__speed['y']

        if self.__position['y'] >= settings.GAME_HEIGHT_PIXELS - self.__height: 
            self.__position['y'] = settings.GAME_HEIGHT_PIXELS - self.__height
            self.__speed['y'] = -self.__speed['y']

        if self.__position['x'] <= 0:
            self.__position['x'] = 0 
            self.__speed['x'] = -self.__speed['x']

        if self.__position['x'] >= settings.GAME_WIDTH_PIXELS-self.__width:
            self.__position['x'] = settings.GAME_WIDTH_PIXELS-self.__width
            self.__speed['x'] = -self.__speed['x']
        
        self.__position['x'] += self.__speed['x']
        self.__position['y'] += self.__speed['y']
        self.__topHitbox = pygame.Rect(self.__position['x'],
                                       self.__position['y'] - self.__height/2, 
                                       self.__width*0.3, 
                                       self.__height*0.1)
        self.__botHitbox = pygame.Rect(self.__position['x'],
                                       self.__position['y'] + self.__height/2, 
                                       self.__width*0.3, 
                                       self.__height*0.1)
        self.__leftHitbox = pygame.Rect(self.__position['x'] - self.__width/2,
                                        self.__position['y'] , 
                                        self.__width*0.1, 
                                        self.__height*0.3)
        self.__rightHitbox = pygame.Rect(self.__position['x'] + self.__width/2,
                                         self.__position['y'] , 
                                         self.__width*0.1, 
                                         self.__height*0.3)






        

