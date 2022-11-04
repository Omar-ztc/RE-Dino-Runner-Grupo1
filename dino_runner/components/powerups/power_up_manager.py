from random import randint
from dino_runner.components.powerups.hammer import Hameer
import pygame
from dino_runner.components.powerups.shield import Shield
class PowerUpManager:
    def __init__(self):
        self.power_ups= []
        self.when_appears = 0
        

    def generate_powerups(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score.score:
            options_powers = randint(0,1)
            if options_powers == 0:
                self.power_ups.append(Shield())
            elif options_powers ==1:
                self.power_ups.append(Hameer())

            self.when_appears += randint(200,300)

    def update(self, game_speed, player, score):
        self.generate_powerups(score)

        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_power_up(power_up.start_time,  power_up.duration, power_up.type)
                self.power_ups.remove(power_up)
                

                


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reser_power_ups(self):
        self.power_ups = []
        self.when_appears = randint(200, 300)