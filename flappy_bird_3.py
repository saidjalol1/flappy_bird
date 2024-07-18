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
pipe_image = pygame.image.load("rasmlar/pipe.png")
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

pipe_gap = 200
pipe_frequency = 5500  # milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency

pipes = []

def create_pipe():
    pipe_height = random.randint(-100, 100)
    bottom_pipe = pipe_image.get_rect(midtop=(screen_width + 100, screen_height // 2 + pipe_height))
    top_pipe = pipe_image.get_rect(midbottom=(screen_width + 100, screen_height // 2 - pipe_gap + pipe_height))
    pipes.append((bottom_pipe, top_pipe))

def move_pipes():
    global pipes
    for pipe in pipes:
        pipe[0].centerx -= scroll_speed
        pipe[1].centerx -= scroll_speed
    pipes = [pipe for pipe in pipes if pipe[0].right > 0]

def draw_pipes():
    for pipe in pipes:
        screen.blit(pipe_image, pipe[0])
        flip_pipe = pygame.transform.flip(pipe_image, False, True)
        screen.blit(flip_pipe, pipe[1])

def check_collision():
    global game_over, flying
    for pipe in pipes:
        if bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1]):
            game_over = True
            flying = False
    if bird_rect.top <= 0 or bird_rect.bottom >= 768:
        game_over = True
        flying = False

def reset_game():
    global bird_rect, bird_speed, flying, game_over, pipes
    bird_rect.center = (100, screen_height // 2)
    bird_speed = 0
    flying = False
    game_over = False
    pipes = []

run  = True
while run:
    
    clock.tick(fps)
    #Bird draw
    #background chizish
    screen.blit(bg, (0,0))
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
            
    if flying: 
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            create_pipe()
            last_pipe = time_now

        move_pipes()
        draw_pipes()
        check_collision()
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

    if game_over:
        screen.blit(restart, (screen_width // 2 - restart.get_width() // 2, screen_height // 2 - restart.get_height() // 2))
        if pygame.mouse.get_pressed()[0] and not flying:
            mouse_pos = pygame.mouse.get_pos()
            if screen_width // 2 - restart.get_width() // 2 < mouse_pos[0] < screen_width // 2 + restart.get_width() // 2 and screen_height // 2 - restart.get_height() // 2 < mouse_pos[1] < screen_height // 2 + restart.get_height() // 2:
                reset_game()
    
    pygame.display.update()
    
    
pygame.quit()