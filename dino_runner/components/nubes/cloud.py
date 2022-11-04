from dino_runner.components.nubes.cloud_game import Cloud_and_entretenimiento
import random

class Cloud(Cloud_and_entretenimiento):
    def __init__(self, images):

        type = random.randint(0,3)
        super().__init__(images, type)
        self.rect.y = 80




