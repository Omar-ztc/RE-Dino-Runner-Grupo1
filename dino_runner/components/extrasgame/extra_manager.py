from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE
from random import randint
import pygame
from dino_runner.components.extrasgame.heart import Heart


class ExtraManager:
    def __init__(self):
        self.extra = []
        self.appears_extra = 0
        self.hearts = 1



    def generate_extras(self, score):
        if len(self.extra) == 0 and self.appears_extra == score.score:
            self.extra.append(Heart())
            self.appears_extra += randint(200,300)



    def update(self,game_speed, player, score):
        self.generate_extras(score)

        for extra_up in self.extra:
            extra_up.update(game_speed, self.extra)
            if player.dino_rect.colliderect(extra_up.rect):
                self.hearts +=1
                self.extra.remove(extra_up)


    def draw(self, screen):
        for extra_up in self.extra:
            extra_up.draw(screen)