import pygame 
from sys import exit

import pygame.image

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 50)
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = font.render('My Game', False, 'Black')
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
x = 400
snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_rect = snail_surface.get_rect(midbottom = (x, 300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if x < 0 :
        x = 400
    else :
        x -= 10
    screen.blit(sky_surface, (0,0))
    screen.blit(ground, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(player_surface, player_rect)
    screen.blit(snail_surface, snail_rect)
    pygame.display.update()
    clock.tick(60)
