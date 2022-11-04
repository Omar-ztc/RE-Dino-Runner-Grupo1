import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_HAMMER,DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD,RUNNING_SHIELD, HAMMER_TYPE, RUNNING_HAMMER,JUMPING_HAMMER

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD,  HAMMER_TYPE: JUMPING_HAMMER }
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }

class Dinosaur(Sprite):
    X_pos = 80
    Y_pos = 310
    JUMP_VELOCITY= 8.5
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()

        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_jump_with_duck = False
        self.jump_velocity = self.JUMP_VELOCITY
        self.power_up_time_up = 0
        self.has_power_up = False


    
    def update(self, user_input):
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        elif self.dino_duck:
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
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_index += 1
   
    def jump(self):
        self.image = JUMP_IMG[self.type]

        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8


        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = self.Y_pos
            self.jump_velocity = self.JUMP_VELOCITY
    
    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type] [1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = 350
        self.step_index += 1 

        
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))

    def on_power_up(self, start_time, duration, type):
        self.has_power_up = True
        self.power_up_time_up = start_time + (duration * 1000)
        self.type = type
        