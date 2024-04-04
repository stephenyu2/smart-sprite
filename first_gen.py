import pygame
import numpy as np
from sys import exit

def display_score():

    current_time = round(pygame.time.get_ticks() / 1000 - start_time, 2)
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Smart Square')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/pixel_type.ttf', 50)
record_font = pygame.font.Font('font/pixel_type.ttf', 25)
player_running_right = False
player_running_left = False
on_surface = True
start_time = 0
last_time = 0
best_time = float('inf')
flag_touched = False

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

rock_surface = pygame.image.load('graphics/rock.png').convert_alpha()
rock_rect = rock_surface.get_rect(midleft = (350, 275))

flag_surface = pygame.image.load('graphics/flag.png').convert_alpha()
flag_rect = flag_surface.get_rect(midbottom = (750, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# ML Initialization
num_steps = 750
num_children = 25
inp = np.random.randint(3, size = (num_children, num_steps))
i = 0
j = 0
scores = np.zeros((1, num_children))
mutate_threshold = .05

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            exit()

    # ML Integration

    if inp[j, i] == 0:

        player_rect.right -= 4

    elif inp[j, i] == 1:

        player_rect.right += 4

    elif on_surface:

        player_gravity -= 20

    i += 1

    if i == inp.shape[1] or flag_rect.colliderect(player_rect):

        scores[0, j] = player_rect.right / i
        player_rect.midbottom = (80, 300)
        i = 0
        j += 1

    if j == inp.shape[0]:

        print(scores)
        index_max = int(np.where(scores == np.max(scores))[1][0])
        index_2max = int(np.where(scores == np.unique(scores)[-2])[1][0])
        parent1 = inp[index_max, :]
        # parent2 = inp[index_2max, :]

        for k in range(inp.shape[1]):

            for l in range(inp.shape[0]):

                # if np.random.rand() > .5:

                inp[l, k] = parent1[k]

                # else:

                    # inp[l, k] = parent2[k]

                if np.random.rand() <= mutate_threshold:

                    inp[l, k] = np.random.randint(3)

        print(parent1)
        j = 0

    # Background
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # Time
    display_score()

    if flag_touched:

        last_time_surf = record_font.render('Last Time: ' + f'{last_time}', False, (64, 64, 64))
        last_time_rect = last_time_surf.get_rect(center = (100, 50))
        screen.blit(last_time_surf, last_time_rect)
        best_time_surf = record_font.render('Best Time: ' + f'{best_time}', False, (64, 64, 64))
        best_time_rect = best_time_surf.get_rect(topleft = (last_time_rect.left, last_time_rect.bottom + 5))
        screen.blit(best_time_surf, best_time_rect)

    # Rock
    screen.blit(rock_surface, rock_rect)

    # Flag
    screen.blit(flag_surface, flag_rect)

    # Player
    player_gravity += 1
    player_rect.bottom += player_gravity
    if player_rect.bottom >= rock_rect.top and player_rect.right > rock_rect.left and player_rect.left < rock_rect.right:

        player_rect.bottom = rock_rect.top
        on_surface = True

    elif player_rect.bottom >= 300:

        player_rect.bottom = 300
        on_surface = True

    else:

        on_surface = False

    screen.blit(player_surface, player_rect)

    # Collision
    if rock_rect.colliderect(player_rect):

        if player_rect.right >= rock_rect.left and player_rect.right <= (rock_rect.left + 5):

            player_rect.right = rock_rect.left

        if player_rect.left <= rock_rect.right and player_rect.left >= (rock_rect.right - 5):

            player_rect.left = rock_rect.right

    if flag_rect.colliderect(player_rect):

        last_time = round(pygame.time.get_ticks() / 1000 - start_time, 4)
        best_time = min(best_time, last_time)
        start_time = pygame.time.get_ticks() / 1000
        flag_touched = True

    pygame.display.update()
    clock.tick(60)