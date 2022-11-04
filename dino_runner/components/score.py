import pygame

from dino_runner.utils.constants import FONT_STYLE

class Score:

    def __init__(self):
        self.score = 0
        self.highest_score = 10


    def update(self, game):
        self.score +=1
        
        if self.score % 100 == 0:
            game.game_speed += 2
            if self.score % 1000 == 0:
               game.game_speed = 40
        
        
        if self.highest_score == self.score:
            self.highest_score +=1

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 20)
        text_component = font.render(f"Points: {self.score}", True, (0,0,0) )
        text_rect = text_component.get_rect()
        text_rect.center = (1000 ,40)
        screen.blit(text_component, text_rect)

        
        text_component2 = font.render(f"Highest score: {self.highest_score}", True, (0,0,0) )
        text_rect = text_component2.get_rect()
        text_rect.center = (800 ,40)
        screen.blit(text_component2, text_rect)
