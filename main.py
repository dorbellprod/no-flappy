import pygame
from player import * # Import EVERYTHING!!
from pygame import Rect
import sys

# Window constants
WIN_SIZE = (800, 700)

# Game constants
PLAYER_W = 80
PLAYER_H = 80
FLAP_SPEED = 15

# Pygame and loop initialization
pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
run = True
clock = pygame.time.Clock()

# Sprites
s_player = pygame.image.load("./brick.jpg")#.convert_alpha()
s_player = pygame.transform.scale(s_player, (PLAYER_W, PLAYER_H))
s_pipe = pygame.image.load("./pipes.png").convert_alpha()

# Fonts
# f_font = pygame.font.Font("Font/Toon Around.otf", 35)
f_font = pygame.font.SysFont(("Agave", "Arial"), 50)


# Player variables
score = 0
score_render = f_font.render(str(score), True, (255, 0, 0))
player = Player(PLAYER_X, 350, PLAYER_W, PLAYER_H)
pipe = Pipe(800 - s_pipe.get_width(), s_pipe.get_width(), s_pipe.get_height())
gravity = 1

while run:
    # Cap frames
    clock.tick(60)

    # Poll events so you don't get "not responding" LOL
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Do logic
                player.yvel = -FLAP_SPEED

    # DRAW ROUTINE - Priority over value updates
    screen.fill((0, 255, 255))
    screen.blit(s_player, (player.x - player.width / 2, player.y - player.height / 2))
    screen.blit(s_pipe, (pipe.x, pipe.y))
    screen.blit(score_render, (0, 0))

    
    # Value updates etc.
    player.update(gravity)
    colliding = pipe.check_collisions(player)
    score_update = pipe.update()
    
    if score_update:
        score += 1
        score_render = f_font.render(str(score), True, (255, 0, 0))

    print(colliding)
    '''
        TODO:
            [X] Pipe Code
            [ ] Game Over
            [ ] Menu?
    '''

    pygame.display.flip()
