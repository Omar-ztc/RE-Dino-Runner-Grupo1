import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import BirdFly
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

import random


class ObstacleManager:
    
    def __init__ (self):
        
        self.obstacles = []



    def update(self, game):
        if len(self.obstacles) == 0:
            self.inventory_obstacle()
          ########

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def update_power_shield(self, game):
        if len(self.obstacles) == 0:
            self.inventory_obstacle()
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
        
    def update_power_Hamer(self, game):
        if len(self.obstacles) == 0:
            self.inventory_obstacle()
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                #pygame.time.delay(300)
                self.obstacles.remove(obstacle)



    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)

    def reset_obstacle(self):
        self.obstacles = []

    def inventory_obstacle (self):
        self.options_obstacles = random.randint(0,2)
        if self.options_obstacles == 0:
                hazar_cactus = "SMALL"
                self.obstacles.append(Cactus(hazar_cactus))
        elif self.options_obstacles == 1:
                hazar_cactus = "LARGE"
                self.obstacles.append(Cactus(hazar_cactus))
        elif self.options_obstacles == 2:
                self.obstacles.append(BirdFly(BIRD))
            

        
