from .obstacle_game import Obstacle
from dino_runner.utils.constants import BIRD
import random
#revisar esta fallamdo
class BirdFly(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(200, 360)
        self.index = 0

    def draw(self, screen):
        if self.index >= 10:
            self.index = 0
        self.type = 0 if self.index <5 else 1
        screen.blit(self.images[self.type], self.rect)    
        self.index += 1

    

