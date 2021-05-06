from random import randint
import settings
from models import blocks
from utils import levels


def build_row(rowindex,placesTo,blocksPos):
    count = 0
    for element in placesTo:        
        if element is None:
            count +=1
            continue
        blocksPos.append({'position': { 'x': count*80,
                                        'y': settings.TOP_BAR_HEIGHT_PIXELS +
                                             (rowindex*40)},
                          'type': element })
        count +=1
    