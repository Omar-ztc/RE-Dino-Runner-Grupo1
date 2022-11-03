import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_large import CactusLarge
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
import random


class ObstacleManager:
    
    def __init__ (self):
        
        self.obstacles = []


    def update(self, game):
        if len(self.obstacles) == 0:
            self.options_obstacles = random.randint(0,2)        ###IMPLEMENTACION
            if self.options_obstacles == 0:
                hazar_cactus = "SMALL"
                self.obstacles.append(Cactus(hazar_cactus))
            elif self.options_obstacles == 1:
                hazar_cactus = "LARGE"
                self.obstacles.append(Cactus(hazar_cactus))
            elif self.options_obstacles == 2:
                self.obstacles.append(CactusLarge(BIRD))

          ########

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)

    def reset_obstacle(self):
        self.obstacles = []
        
