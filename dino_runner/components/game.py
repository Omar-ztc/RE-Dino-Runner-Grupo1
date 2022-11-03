import pygame
import dino_runner
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacles_manager import ObstacleManager
from dino_runner.components.nubes.cloud_manager import EntretenimientoManager      
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,FONT_STYLE,RESET
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.score import Score


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
        self.number_game= 0
        self.score = Score()


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
        self.obstacle_manager.update(self)
        self.entretenimiento_manager.update(self)  ###implementacion      cambiar a entretenimiento
        self.score.update(self)


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 255, 0))
        if self.score.score >=300:       #implementacion
            self.screen.fill((255, 255, 255))

        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self)
        self.entretenimiento_manager.draw(self)      
        self.score.draw(self.screen)
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
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        #mostrar mensaje de bienvenida
        if self.number_game <1:
          font = pygame.font.Font(FONT_STYLE, 30)
          text_component = font.render("Press any key to play", True, (0,0,0) )
          text_rect= text_component.get_rect()
          text_rect.center = (half_screen_width, half_screen_height)
          self.screen.blit(text_component,(text_rect))
        else:
          font = pygame.font.Font(FONT_STYLE, 30)
          font2 = pygame.font.Font(FONT_STYLE, 24)
          text_component = font.render("Moriste!!! presione tecla para volver a jugar", True, (0,0,0) )
          text_component2 = font2.render(("Your number death count is : "+ str(self.number_game)), True, (0,0,0) )
          text_rect= text_component.get_rect()
          text_rect.center = (half_screen_width, half_screen_height)
          text_rect2= text_component.get_rect()
          text_rect2.center = (half_screen_width+117, half_screen_height+100)
          self.screen.blit(text_component,(text_rect))
          self.screen.blit(text_component2,(text_rect2))
          self.screen.blit(RESET[0],(half_screen_width-40,half_screen_height +140 ))
        #mostrar mensaje de volver a jugar
        #mostrar un icono
        self.screen.blit(RUNNING[0], (half_screen_width-40, half_screen_height - 140 ))
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



