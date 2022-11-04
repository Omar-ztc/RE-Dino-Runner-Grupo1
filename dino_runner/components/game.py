import pygame
import dino_runner
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.nubes.cloud_manager import EntretenimientoManager      
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE,RESET,DINOTRISTE, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.score import Score
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.powerups.shield import Shield

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.entretenimiento_manager = EntretenimientoManager()   
        self.power_ups_manager = PowerUpManager()    
        self.number_game= 0
        self.score = Score()
        self.shields = [Shield()]



    def execute(self):
        self.executing = True
        
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacle()
        self.number_game += 1
        self.score.score = 0
        self.game_speed = 20 
        
        self.power_ups_manager.reser_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        if self.player.has_power_up:
            if self.player.type == SHIELD_TYPE:
                self.obstacle_manager.update_power_shield(self)
            else:
                self.obstacle_manager.update_power_Hamer(self)

        else :
            self.obstacle_manager.update(self)


        self.entretenimiento_manager.update(self)  ###implementacion      cambiar a entretenimiento
        self.score.update(self)
        self.power_ups_manager.update(self.game_speed, self.player,self.score)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        if self.score.score >=400:       #implementacion
            self.screen.fill((128, 128, 128))
        if self.score.score >= 1000:
            self.screen.fill((94, 54, 30))

        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self)
        self.entretenimiento_manager.draw(self)      
        self.score.draw(self.screen)
        self.power_ups_manager.draw(self.screen)
        self.draw_power_up_active()

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def show_menu(self):
        #pintar la ventana
        #self.screen.fill((128, 128, 128))
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        #mostrar mensaje de bienvenida
        if self.number_game <1:
          self.screen.fill((255,255,255))
          font = pygame.font.Font(FONT_STYLE, 30)
          text_component = font.render("Press any key to play", True, (0,0,0) )
          text_rect= text_component.get_rect()
          text_rect.center = (half_screen_width, half_screen_height + 180)
          self.screen.blit(text_component,(text_rect))
          self.screen.blit(DINOTRISTE[0], (half_screen_width-200, half_screen_height - 270 ))
        else:
          font = pygame.font.Font(FONT_STYLE, 30)
          font2 = pygame.font.Font(FONT_STYLE, 24)
          self.screen.fill((0, 0, 0))
          text_component = font.render("Moriste!!! presione tecla para volver a jugar", True, (255,255,255) )
          text_component2 = font2.render((" # death count = "+ str(self.number_game)), True, (255,255,255) )
          text_component3 = font2.render(("score = "+ str(self.score.score)), True, (255,255,255) )
          text_component4 = font2.render(("highest score = "+ str(self.score.highest_score)), True, (255,255,255) )
          text_rect= text_component.get_rect()
          text_rect.center = (half_screen_width, half_screen_height+80)
          text_rect2= text_component.get_rect()
          text_rect2.center = (half_screen_width+210, half_screen_height+250)
          text_rect3= text_component.get_rect()
          text_rect3.center = (half_screen_width+600, half_screen_height+250)
          text_rect4= text_component.get_rect()
          text_rect4.center = (1150,30)
          self.screen.blit(text_component,(text_rect))
          self.screen.blit(text_component2,(text_rect2))
          self.screen.blit(text_component3,(text_rect3))
          self.screen.blit(text_component4,(text_rect4))
          self.screen.blit(RESET[0],(half_screen_width-40,half_screen_height +120 ))
          self.screen.blit(DINOTRISTE[1], (half_screen_width-150, half_screen_height - 275 ))
        #mostrar mensaje de volver a jugar

        #actualizar evento
        pygame.display.update()
        #escuchar evento
        self.handle_key_event_on_menu()

    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False

            elif event.type == pygame.KEYDOWN:
                self.run()

    def draw_power_up_active(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000)
            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 15)
                powerup_text = font.render(f"time left: {time_to_show} ", True, (0,0,0) )
                self.screen.blit(powerup_text, (80,420))
                pygame.display.update()
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE