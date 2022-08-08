import pygame
from player import * # Import EVERYTHING!!
from pygame import Rect
import sys

# Window constants
WIN_SIZE = (800, 700)

# Game constants
PLAYER_W = 80
PLAYER_H = 80
FLAP_SPEED = 12

# Pygame and loop initialization
pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Poly Flap DREAM Tutorial!", )
run = True
clock = pygame.time.Clock()

# Sprites
s_player = pygame.image.load("./brick.jpg")#.convert_alpha()
s_player = pygame.transform.scale(s_player, (PLAYER_W, PLAYER_H))
s_pipe = pygame.image.load("./pipes.png").convert_alpha()
pygame.display.set_icon(s_player)

# Fonts
# f_font = pygame.font.Font("Font/Toon Around.otf", 35)
f_font = pygame.font.SysFont(("Comic Sans", "Arial"), 50, True)
f_bigfont = pygame.font.SysFont(("Comic Sans", "Arial"), 100, True)


# Player variables
score = 0
player = Player(PLAYER_X, 350, PLAYER_W, PLAYER_H)
pipe = Pipe(800 - s_pipe.get_width(), s_pipe.get_width(), s_pipe.get_height())
gravity = 1

# Text rendering
score_render = f_font.render(str(score), True, (0, 0, 0))
game_over_render = f_bigfont.render("Game Over! L", True, (0, 0, 0))
press_space_render = f_font.render("Press Space to retry", True, (0, 0, 0))

game_scene = True
game_over = False
while run:
    while game_scene: # Game state
        # Cap frames
        clock.tick(60)

        # Poll events so you don't get "not responding" LOL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_scene = False
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
            score_render = f_font.render(str(score), True, (0, 0, 0))

        if colliding or player.y > WIN_SIZE[1]:
            game_scene = False
            game_over = True
        '''
            TODO:
                [X] Pipe Code
                [X] Game Over
        '''
        pygame.display.flip()
    while game_over: # Game Over state
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Restart the game
                    # Also reset values
                    score = 0
                    score_render = f_font.render(str(score), True, (0, 0, 0))
                    player = Player(PLAYER_X, 350, PLAYER_W, PLAYER_H)
                    pipe = Pipe(800 - s_pipe.get_width(), s_pipe.get_width(), s_pipe.get_height())

                    game_over = False
                    game_scene = True

        screen.fill((255, 255, 255))
        screen.blit(game_over_render, (25, 25))
        screen.blit(
            f_font.render(f"Your score was {score}", True, (0, 255, 0)),
            (25, 200)
        )
        screen.blit(press_space_render, (25, 340))
        pygame.display.flip()