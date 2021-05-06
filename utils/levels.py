from random import randint
import settings
from models import blocks
from utils import mapBuild


################################################################################
################################    LEVELS   ###################################
################################################################################

def l_3():    
    blocksPos = []
    blocksPos.append({'position': { 'x': 10,
                                    'y': 10},
                      'type': 0 })
    return blocksPos

def l_2():    
    blocksPos = []
    placesTo = [None,None,None,0,0,0,None,None,None]
    mapBuild.build_row(3, placesTo,blocksPos)

    placesTo = [None,None,0,0,1,0,0,None,None]
    mapBuild.build_row(4, placesTo,blocksPos)

    placesTo = [None,0,0,1,2,1,0,0,None]
    mapBuild.build_row(5, placesTo,blocksPos)

    placesTo = [None,None,0,0,1,0,0,None,None]
    mapBuild.build_row(6, placesTo,blocksPos)

    placesTo = [None,None,None,0,0,0,None,None,None]
    mapBuild.build_row(7, placesTo,blocksPos)

    return blocksPos


def l_1():    
    blocksPos = []
    placesTo = [0,0,0,0,1,None,None,None,None]
    mapBuild.build_row(0, placesTo,blocksPos)

    placesTo = [None,None,None,None,2,0,0,0,0]
    mapBuild.build_row(1, placesTo,blocksPos)

    placesTo = [0,0,0,0,1,None,None,None,None]
    mapBuild.build_row(2, placesTo,blocksPos)

    placesTo = [None,None,None,None,2,0,0,0,0]
    mapBuild.build_row(3, placesTo,blocksPos)

    placesTo = [0,0,0,0,1,None,None,None,None]
    mapBuild.build_row(4, placesTo,blocksPos)

    placesTo = [None,None,None,None,2,0,0,0,0]
    mapBuild.build_row(5, placesTo,blocksPos)

    placesTo = [0,0,0,0,1,None,None,None,None]
    mapBuild.build_row(6, placesTo,blocksPos)

    placesTo = [None,None,None,None,2,0,0,0,0]
    mapBuild.build_row(7, placesTo,blocksPos)

    
    
    return blocksPos

def l_4():    
    blocksPos = []

    for i in range(0,settings.GAME_WIDTH_PIXELS-settings.TOP_BAR_HEIGHT_PIXELS,80):
            for j in range(settings.TOP_BAR_HEIGHT_PIXELS,int(settings.GAME_HEIGHT_PIXELS/2),40):
                blocksPos.append({'position': { 'x': i,
                                                'y': j},
                                  'type': randint(0,1) })
    return blocksPos

################################################################################
################################################################################
################################################################################

#constr is a list of callable of blocks constructor
constr = []
constr.append(blocks.Block1.Block1)
constr.append(blocks.Block2.Block2)
constr.append(blocks.Block3.Block3)


#blocksMapper is a list that contains the required map that allows ->
#-> previous constructors to build blocks. Each element is a level
blocksMapper = []
blocksMapper.append(l_1())
blocksMapper.append(l_2())
blocksMapper.append(l_3())
blocksMapper.append(l_4())



def builder(levelindex):
    blocksList = []
    blocks_map = blocksMapper[levelindex]
    for i in range(len(blocks_map)):
        blocksList.append(constr[blocks_map[i]['type']](blocks_map[i]['position']))
    
    return blocksList









