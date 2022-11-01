import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur(Sprite):
    X_pos = 80
    Y_pos = 310
    JUMP_VELOCITY= 8.5


    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = self.JUMP_VELOCITY

    
    def update(self, user_input):
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        else:
            self.duck()
        
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump= True
            self.dino_run = False


        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
        
        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run = False

        
        
        elif not self.dino_duck:
            self.dino_duck = False
            self.dino_run = True


        if self.step_index >=10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index += 1
   
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8


        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_pos
            self.jump_velocity = self.JUMP_VELOCITY
    
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = 350
        self.step_index += 1 



        
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))