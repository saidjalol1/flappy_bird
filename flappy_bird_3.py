import random
import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

#load images
bg = pygame.image.load("rasmlar/bg.png")
ground = pygame.image.load("rasmlar/ground.png")
pipe = pygame.image.load("rasmlar/pipe.png")
restart = pygame.image.load("rasmlar/restart.png")


bird_images = [
    pygame.image.load('rasmlar/bird1.png'),
    pygame.image.load('rasmlar/bird2.png'),
    pygame.image.load('rasmlar/bird3.png')
]




bird_index = 0
bird_rect = bird_images[0].get_rect()
bird_rect.center = (100, screen_height // 2)
bird_speed = 0
jump_velocity = -10
flying = False
game_over = False
# game_veraiables
ground_scroll = 0
scroll_speed = 4

pipe_image = pygame.image.load('rasmlar/pipe.png').convert_alpha()
pipe_width = pipe_image.get_width()
pipe_height = pipe_image.get_height()

PIPE_GAP = 150
PIPE_SPEED = 3
SPAWN_PIPE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_PIPE_EVENT, 1200)

pipes = []

def create_pipe():
    gap_y = random.randint(100, screen_height - 100 - PIPE_GAP)
    top_pipe = pipe_image.get_rect(midbottom=(screen_width, gap_y))
    bottom_pipe = pipe_image.get_rect(midtop=(screen_width, gap_y + PIPE_GAP))
    return top_pipe, bottom_pipe

def move_and_draw_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= PIPE_SPEED
        if pipe.top < 0:  # This is the top pipe
            flipped_pipe = pygame.transform.flip(pipe_image, False, True)
            screen.blit(flipped_pipe, pipe)
        else:  # This is the bottom pipe
            screen.blit(pipe_image, pipe)
    return [pipe for pipe in pipes if pipe.right > 0]

run  = True
while run:
    
    clock.tick(fps)
    #Bird draw
    #background chizish
    screen.blit(bg, (0,0))
    pipes = move_and_draw_pipes(pipes)
    #yerni chizish
    screen.blit(ground, (ground_scroll, 768))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP and flying == True:
            if event.button == 1:
                flying = True
                bird_speed = -10
        elif event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            if event.button == 1:
                flying = True
        elif event.type == SPAWN_PIPE_EVENT:
            pipes.extend(create_pipe())
            
    if flying:        
        if bird_rect.y < 768:
            bird_rect.y += bird_speed
        bird_speed += 0.5
        if bird_speed > 8:
            bird_speed = 8
    
    if bird_rect.bottom > 768:
        game_over = True
        flying = False
        
    if game_over == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
            
    screen.blit(bird_images[bird_index], bird_rect)
    bird_index = (bird_index + 1) % len(bird_images)
    
        
    
    pygame.display.update()
    
    
pygame.quit()