from .obstacle_game import Obstacle
import random

class CactusLarge(Obstacle):
    def __init__(self, images):
        type = random.randint(0,2)
        super().__init__(images, type)
        self.rect.y = 305                 ##la medida buena es 305 por ahi
