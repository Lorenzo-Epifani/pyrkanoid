import pygame
import settings
from models.BarModel import BarModel
from models.LevelModel import LevelModel
from models.BallModel import BallModel
from numpy import sign


class GameModel:

#implement start level
    def __init__(self):
        pygame.font.init()
        self.__score = 0
        self.__level = LevelModel()
        self.__bar = BarModel()
        self.__ball = []        
        self.__ball.append(BallModel())
        self.__lives = 3
        

    @property
    def score(self):
        return self.__score

    @property
    def level(self):
        return self.__level

    @property
    def lives(self):
        return self.__lives

    @property
    def ball(self):
        return self.__ball

    @property
    def bar(self):
        return self.__bar
#PROVVISORY----> IMPLEMENT AN INTERACTION MANAGER
    def update_game(self):
        self.__bar.updatePos()
        for element in self.__ball:    
            element.updatePos()            
            barBotColl=element.botHitbox.colliderect(self.__bar.hitbox)
            barLeftColl=element.leftHitbox.colliderect(self.__bar.hitbox)
            barRightColl=element.rightHitbox.colliderect(self.__bar.hitbox)

            if  barBotColl or barLeftColl or barRightColl:
                if sign(element.speed['x'] + self.__bar.speed)*(element.speed['x'] + self.__bar.speed) >= 15:
                    element.speed['x'] = 15*sign(element.speed['x'] + self.__bar.speed)
                else:
                    element.speed['x'] += self.__bar.speed
                if  barBotColl:
                    element.speed['y'] = -element.speed['y']
                if  barLeftColl or barRightColl:
                    element.speed['x'] = -element.speed['x']
        
            #print(range(len(self.__level.blocks)))
            rem=0
            for i in range(len(self.__level.blocks)):
                blockTopColl=element.topHitbox.colliderect(self.__level.blocks[i-rem].hitbox)
                blockBotColl=element.botHitbox.colliderect(self.__level.blocks[i-rem].hitbox) 
                blockLeftColl=element.leftHitbox.colliderect(self.__level.blocks[i-rem].hitbox)
                blockRightColl=element.rightHitbox.colliderect(self.__level.blocks[i-rem].hitbox)

                if  blockTopColl or blockBotColl or blockLeftColl or blockRightColl:
                    if self.__level.blocks[i-rem].hit() <= 0:
                        del self.__level.blocks[i-rem]
                        rem +=1
                        #self.__ball.append(BallModel())
                        if len(self.__level.blocks) == 0:
                            self.__level.next()
                            element = BallModel()
                    if blockTopColl or blockBotColl:
                        element.speed['y'] = -element.speed['y']
                    if blockLeftColl or blockRightColl:
                        element.speed['x'] = -element.speed['x']
                
                

                 



        

        

