from random import randint
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Extras(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 800
        self.rect.y = randint(125,350)

    
    def update(self, game_speed, extras_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            extras_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)    
