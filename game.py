import pygame
import numpy as np
from sys import exit
from third_gen import neural

class game: 

    def __init__(self): 

        pass

    def get_inputs(self): 

        player_height = self.player_rect.bottom
        distance_to_nearest_obstacle_on_right = self.rock_rect.left - self.player_rect.right
        distance_to_flag = self.flag_rect.left - self.player_rect.right
        return [player_height, distance_to_nearest_obstacle_on_right, distance_to_flag] 
    
    def get_input_dimension(self): 

        return len(self.get_inputs())  

    def display_score(self):

        self.current_time = round(self.elapsed_time / 1000, 2)
        self.score_surf = self.test_font.render(f'{self.current_time}', False, (64, 64, 64))
        self.score_rect = self.score_surf.get_rect(center = (400, 50))
        self.screen.blit(self.score_surf, self.score_rect)

    def level1(self): 

        self.rock_rect = self.rock_surface.get_rect(midleft = (350, 275))
        self.flag_rect = self.flag_surface.get_rect(midbottom = (750, 300))
        self.player_rect = self.player_surface.get_rect(midbottom = (80, 300))
        ## Try to show screen before running epoch
        
    def start(self, level): 

        self.level = level
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Smart Square')
        self.clock = pygame.time.Clock()
        self.test_font = pygame.font.Font('font/pixel_type.ttf', 50)
        self.record_font = pygame.font.Font('font/pixel_type.ttf', 25)
        self.on_surface = True
        self.start_time = 0
        self.last_time = 0
        self.best_time = float('inf')
        self.flag_touched = False

        self.sky_surface = pygame.image.load('graphics/sky.png').convert()
        self.ground_surface = pygame.image.load('graphics/ground.png').convert()
        self.rock_surface = pygame.image.load('graphics/rock.png').convert_alpha()
        self.flag_surface = pygame.image.load('graphics/flag.png').convert_alpha()
        self.player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()

        self.player_gravity = 0

        if(self.level == 1): 

            self.level1()

    def play_epoch(self, model): 

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()
            
            # Elapsed time
            self.elapsed_time = pygame.time.get_ticks() - self.start_time

            # Player movement
            inputs = self.get_inputs() 
            direction_probability_array = model.direction(inputs)
            direction = np.argmax(direction_probability_array)

            if direction == 0:

                self.player_rect.right -= 4

            elif direction == 1:

                self.player_rect.right += 4

            elif self.on_surface:

                self.player_gravity -= 20

            # Reward function
            if self.flag_rect.colliderect(self.player_rect) or self.elapsed_time >= 10000: 

                reward = self.player_rect.right
                self.start(level = self.level) 
                self.start_time = pygame.time.get_ticks() 
                return reward ## Need to account for making it to end before 10 seconds

            # Background
            self.screen.blit(self.sky_surface, (0, 0))
            self.screen.blit(self.ground_surface, (0, 300))

            # Time
            self.display_score()

            # Rock
            self.screen.blit(self.rock_surface, self.rock_rect)

            # Flag
            self.screen.blit(self.flag_surface, self.flag_rect)

            # Player
            self.player_gravity += 1
            self.player_rect.bottom += self.player_gravity
            if self.player_rect.bottom >= self.rock_rect.top and self.player_rect.right > self.rock_rect.left and self.player_rect.left < self.rock_rect.right:

                self.player_rect.bottom = self.rock_rect.top
                self.on_surface = True

            elif self.player_rect.bottom >= 300:

                self.player_rect.bottom = 300
                self.on_surface = True

            else:

                self.on_surface = False

            self.screen.blit(self.player_surface, self.player_rect)

            # Collision
            if self.rock_rect.colliderect(self.player_rect):

                if self.player_rect.right >= self.ock_rect.left and self.player_rect.right <= (self.rock_rect.left + 5):

                    self.player_rect.right = self.rock_rect.left

                if self.player_rect.left <= self.rock_rect.right and self.player_rect.left >= (self.rock_rect.right - 5):

                    self.player_rect.left = self.rock_rect.right

            pygame.display.update()
            self.clock.tick(60)