import pygame 
from sys import exit

import pygame.image

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = True
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert_alpha()

score_surface = font.render('My Game', False, (64,64,64))
score_rect = score_surface.get_rect(center = (400, 50))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_rect = snail_surface.get_rect(midbottom = (500, 300))

player_gravity = -20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground, (0, 300))
        pygame.draw.rect(screen,'#c0e8ec', score_rect)
        pygame.draw.rect(screen,'#c0e8ec', score_rect, 10)
        # pygame.draw.line(screen, 'Red', (0,0), (800,400))
        screen.blit(score_surface, score_rect)

        #player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0 : 
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        if player_rect.colliderect(snail_rect):
            game_active = False
    
    else:
        screen.fill('Yellow')
    pygame.display.update()
    clock.tick(60)
