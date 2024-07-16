import pygame 
from sys import exit
from random import randint

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for ele in obstacle_list:
            ele.x -= 5
            if ele.bottom == 300:
                screen.blit(snail_surface, ele)
            else:
                screen.blit(fly_surface, ele)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else :
        return []
    
def collisions(obstacle_list, player):
    if obstacle_list:
        for ele in obstacle_list:
            if ele.colliderect(player):
                return False
        return True
    return True

def player_animation():
    global player_surface, player_index
    
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk) : player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = False
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert_alpha()

#score_surface = font.render('My Game', False, (64,64,64))
#score_rect = score_surface.get_rect(center = (400, 50))

player_walk_1= pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2= pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
player_index = 0
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))

snail_frame1 = pygame.image.load('graphics/snail/snail1.png')
snail_frame2 = pygame.image.load('graphics/snail/snail2.png')
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_surface1 = pygame.image.load('graphics/Fly/Fly1.png')
fly_surface2 = pygame.image.load('graphics/Fly/Fly2.png')
fly_frames = [fly_surface1, fly_surface2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

player_gravity = -20
start_time = 0
score = 0
obstacle_rect_list = []
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer, 500)

fly_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_timer, 200)

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0,2)
player_stand_rect = player_stand.get_rect(center = (400, 200))


game_name = font.render('Pixel Runner', False , (64,64,64))
game_name_rect = game_name.get_rect(center = (400, 80))

start_text = font.render('CLICK SPACE TO START', False , (64,64,64))
start_text_rect = start_text.get_rect(center = (400, 330))

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score : {current_time}', False, (111,196,169))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time
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
            if event.type == obstacle_timer:
                if(randint(0,2)):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900,1100), 200)))
            if event.type == snail_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else : snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            if event.type == fly_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else : fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground, (0, 300))

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        #pygame.draw.rect(screen,'#c0e8ec', score_rect)
        #pygame.draw.rect(screen,'#c0e8ec', score_rect, 10)
        # pygame.draw.line(screen, 'Red', (0,0), (800,400))
        #screen.blit(score_surface, score_rect)
        score = display_score()
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        player_animation()
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # snail_rect.x -= 4
        # if snail_rect.right <= 0 : 
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)
        game_active = collisions(obstacle_rect_list, player_rect)
        # if player_rect.colliderect(snail_rect):
        #     game_active = False
    
    else:
        screen.fill((94,129,162))
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        screen.blit(player_stand, player_stand_rect)
        if score == 0:
            screen.blit(start_text, start_text_rect)
        else:
            score_surface = font.render(f'Score: {score}', False, (111,196,169))
            score_surface_rect = score_surface.get_rect(center = (400, 330))
            screen.blit(score_surface, score_surface_rect)
        screen.blit(game_name, game_name_rect)
    pygame.display.update()
    clock.tick(60)
