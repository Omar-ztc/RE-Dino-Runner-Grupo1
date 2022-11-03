import pygame
from dino_runner.components.nubes.cloud import Cloud

from dino_runner.utils.constants import BIRD, SMALL_CACTUS,CLOUD, ENTRETENIMIENTO
import random


class EntretenimientoManager:
    
    def __init__ (self):
        self.entreteming = []
  


    def update(self, game):
        if len(self.entreteming) == 0:
            self.entreteming.append(Cloud(ENTRETENIMIENTO))



        for photo in self.entreteming:
            photo.update(game.game_speed, self.entreteming)
           

    def draw(self, game):
        for photo in self.entreteming:
            photo.draw(game.screen)