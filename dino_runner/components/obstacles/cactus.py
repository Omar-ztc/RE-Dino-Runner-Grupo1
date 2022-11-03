from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from .obstacle_game import Obstacle
import random

class Cactus(Obstacle):
    CACTUS_OPTIONS = {
        "SMALL" : (SMALL_CACTUS, 325),
        "LARGE" : (LARGE_CACTUS, 300)
    }
 

    def __init__(self, hazar_cactus ):
 
        images, posicion_y = self.CACTUS_OPTIONS[hazar_cactus]
        type = random.randint(0,2)
        super().__init__(images, type)
        self.rect.y = posicion_y


